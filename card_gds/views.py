from django.shortcuts import render
from http import cookies
import uuid
import time
import base64
import json
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from card_gds.models import Cards
import logging

logger = logging.getLogger(__name__)


class CardsDetailView(DetailView):
    model = Cards
    template_name = 'cards/detail.html'


class CardsListView(ListView):
    model = Cards

    template_name = 'product/list.html'
    context_object_name = 'cards'

    paginate_by = 3

    s = dict()

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

        return qs

    def get_queryset(self):
        qs = super().get_queryset()
        category_name = self.request.GET.get('category_name', None)
        if category_name:
            qs = qs.filter(category__category__slug=category_name)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Товары'

        return context

    def post(self, request, *args, **kwargs):

        category_name = self.request.GET.get('category_name', None)

        if category_name:
            model = Cards.objects.filter(category__category__slug=category_name)
        else:
            model = Cards.objects.all()
        st = render(request, self.template_name, {'cards': model})
        logger.info(st)

        ts = int(time.time())

        try:
            basketid = self.request.COOKIES["BasketID"]
        except:
            basketid = None

        try:

            s = request.COOKIES["w"]
            s = cookies.SimpleCookie(request.COOKIES)
            s = s.get("w").value
            logger.info(request.session())
        except:

            logger.info(request.COOKIES["w"])

            logger.info(type(request.COOKIES["w"]))
        if s == "":
            s = dict()
            s['orderid'] = basketid
            logger.info("s = dict()")
        else:

            s = s.encode()
            s = base64.b64decode(s).decode('utf-8')
            s = json.loads(s)

        s[ts] = {"id": request.POST['cardsID'],
                 "count": 1,
                 "price": model.get(id=request.POST['cardsID']).price,
                 "name": model.get(id=request.POST['cardsID']).name,
                 "category": model.get(id=request.POST['cardsID']).category.name,
                 "photo": model.get(id=request.POST['cardsID']).photo.url,
                 }
        s = json.dumps(s)
        logger.info(s)
        encoded = base64.b64encode(s.encode('utf-8'))

        st.cookies['w'] = encoded.decode("utf-8")
        st.cookies["w"]["path"] = "/"

        st.cookies["w"]["httponly"] = 1

        st.cookies["id"] = request.POST['cardsID']
        st.cookies["id"]["path"] = "/"

        st.cookies["id"]["httponly"] = 1

        st.cookies.output()
        return st


def auther(request):
    if request.POST and ("auth" not in request.session):

        logger.info("пользователь не загистрирован")
    elif request.POST and (request.session["auth"] == False):

        logger.info("войти в личный кабинет")
    elif request.POST and (request.session["auth"] == True):

        logger.info("LogOut")
