from django.shortcuts import render, redirect
from http import cookies
import uuid
import base64
import json
from basket.forms import ModelOrderItemsForm, ModelOrderForm
from basket.models import Order, OrderItems
from django.contrib import messages

from django.views.generic.list import ListView


import logging

logger = logging.getLogger(__name__)


class OrderView(ListView):
    model = OrderItems
    template_name = 'shopping_cart/shopping_cart.html'
    context_object_name = 'cards'

    def get(self, request, *args, **kwargs):
        qs = super().get(request, *args, **kwargs)
        if "BasketID" not in self.request.COOKIES:
            st = cookies.SimpleCookie(self.request.COOKIES)
            qs.cookies['BasketID'] = str(uuid.uuid4())
            qs.cookies["BasketID"]["path"] = "/"
            qs.cookies["BasketID"]["httponly"] = 1
            qs.cookies['w'] = ""
            qs.cookies["w"]["path"] = "/"

            qs.cookies["w"]["httponly"] = 1

            qs.cookies.output()

            logger.info(self.request.COOKIES)

            self.s = dict()
        try:
            s = request.COOKIES["w"]
        except:
            logger.info(request.COOKIES["w"])
            s = None
        if s == "" or s is None:
            message = "Чтото не так"
            return message
        else:
            logger.info("__name__ ", __name__)
            s = s.encode()
            s = base64.b64decode(s).decode('utf-8')
            s = json.loads(s)
        logger.info(s)
        try:
            r = len(s) - 1
            for k, v in s.items():
                logger.info(f'key={k}, value={v}')
        except:
            logger.info("ror")
        return render(request, self.template_name, {'cards': s, 'carts': r})


def bascet_user_apply(request):
    if request.method == "POST":
        form = ModelOrderForm(request.POST)
        if form.is_valid():
            instance = form.save()
            logger.info(u'%s' % instance)
            messages.success(request, "Saved!")
            return redirect('basket:list')
    else:
        form = ModelOrderForm()
    return render(request, 'shopping_cart/forms/apply.html', {'form': form})


def bascet_user_apply_edit(request, pk):
    basket_user = Order.objects.get(id=pk)
    if request.method == "POST":
        form = ModelOrderForm(request.POST, instance=basket_user)
        if form.is_valid():
            basket_user = form.save()
            messages.success(request, "Saved Edit!")
            return redirect('basket:list')
    else:
        form = ModelOrderForm(instance=basket_user)
    return render(request, 'shopping_cart/forms/basket_user_edit.html', {'form': form})


def bascet_user_apply_delete(request, pk):
    basket_user = Order.objects.get(id=pk)
    if request.method == "POST":
        basket_user.delete()
        messages.success(request, "Deleted!")
        return redirect('basket:list')
    return render(request, 'shopping_cart/forms/basket_user_delete.html', {'basket_user': basket_user})


def basket_order_apply_delete(request, pk):
    st = redirect('basket:order')
    try:
        s = request.COOKIES["w"]
    except:
        logger.info(request.COOKIES["w"])
        s = None
    if s == "" or s is None:
        message = "Чтото не так"
        return message
    else:
        s = s.encode()
        s = base64.b64decode(s).decode('utf-8')
        s = json.loads(s)
    logger.info(s)
    order = s[pk]["name"]
    if request.method == "POST":
        try:
            del s[pk]
            s = json.dumps(s)
            encoded = base64.b64encode(s.encode('utf-8'))

            st.cookies['w'] = encoded.decode("utf-8")
            st.cookies["w"]["path"] = "/"

            st.cookies["w"]["httponly"] = 1
            messages.success(request, "Deleted!")
        except:
            messages.success(request, "Not found!")
        return st
    return render(request, 'shopping_cart/forms/basket_user_delete.html', {'basket_user': order})


def bascet_order_save(request):
    try:
        s = request.COOKIES["w"]
    except:
        logger.info(request.COOKIES["w"])
        s = None
    if s == "" or s is None:
        message = "Чтото не так"
        return message
    else:
        s = s.encode()
        s = base64.b64decode(s).decode('utf-8')
        s = json.loads(s)
    logger.info(s)
    if request.method == "POST":
        try:

            for k, v in s.items():
                logger.info(f'key={k}, value={v}')
                if k != "orderid":
                    oi = OrderItems(
                        nameid=v["id"],
                        name=v["name"],
                        category=v["category"],
                        price=v["price"],
                        quantity=v["count"],
                        orderid=s["orderid"],
                    )
                    oi.save()

        except:
            logger.info("ror")
        return render(request, "shopping_cart/order_complete.html")
    messages.success(request, "Карзина пуста!")
    return render(request, "shopping_cart/shopping_cart.html")


def bascet_card_add(request):
    pass


def bascet_card_apply(request):
    if request.method == "POST":

        form = ModelOrderForm(request.POST)

        if form.is_valid():
            basket_user = form.save()

            messages.success(request, "Saved!")

            st = render(request, 'basket/forms/apply.html', {'form': form})

            return st

    else:

        try:
            basketid = request.COOKIES["BasketID"]

        except:
            basketid = None

        form = ModelOrderForm(initial={"orderid": basketid})
    return render(request, 'basket/forms/apply.html', {'form': form})


def bascet_card_apply_edit(request, pk):
    basket_user = Order.objects.get(id=pk)
    if request.method == "POST":

        form = ModelOrderItemsForm(request.POST, instance=basket_user)

        if form.is_valid():
            basket_user = form.save()

            messages.success(request, "Saved Edit!")
            return redirect('basket:list')
    else:
        form = ModelOrderItemsForm(instance=basket_user)
    return render(request, 'basket/forms/basket_user_edit.html', {'form': form})


def bascet_card_apply_delete(request, pk):
    basket_user = Order.objects.get(id=pk)
    if request.method == "POST":
        basket_user.delete()
        messages.success(request, "Deleted!")
        return redirect('basket:list')
    return render(request, 'basket/forms/basket_user_delete.html', {'basket_user': basket_user})


def basket_card_admin(request):
    if request.session["auth"]:
        basket_user = Order.objects.all()
        return render(request, 'old/basket/forms/list_all.html', {'basket_user': basket_user})
    else:
        return redirect('users:list')


def basket_card_admin_detail(request, uuid):
    try:
        if request.method == "POST":

            basket_user = OrderItems.objects.filter(orderid=uuid)
            return render(request, 'old/basket/forms/list_all.html', {'basket_user': basket_user})
        else:
            return render('users:list')
    except:
        return redirect('cards:basket')
