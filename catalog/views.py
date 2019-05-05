from django.shortcuts import render
from django.views.generic.list import ListView
from catalog.models import Category, SubCategory
from card_gds.models import Cards, Partners, Baners
from django.core.paginator import Paginator
import base64
import json

import logging

logger = logging.getLogger(__name__)


def CatalogDetailView(request, pk):
    catalog = Cards.objects.filter(category=pk)
    return render(request, 'catalog/detail.html', {'catalogs': catalog})


class CatalogListView(ListView):
    model = SubCategory
    template_name = 'catalog/list.html'
    context_object_name = 'catalogs'

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.GET.get('catalog_id', None)
        if category_id:
            qs = qs.filter(categorys_id=category_id)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Каталог'
        return context


def index(request):
    categories = Category.objects.filter(is_active=True)
    best_sales = Cards.objects.filter(best_sales=True).filter(is_active=True)
    cat_index = Category.objects.filter(is_index=True)
    trasted_partners = Partners.objects.filter(trusted=True).filter(is_active=True)
    baners = Baners.objects.filter(is_active=True)
    return render(request, 'index.html',
                  {"categories": categories, "best_sales": best_sales, "trasted_partners": trasted_partners,
                   "baners": baners, "cat_indexes": cat_index})


def subcat(request, name):
    cards_list = Cards.objects.filter(category__category__slug=name)
    paginator = Paginator(cards_list, 3)

    page = request.GET.get('page')
    cards = paginator.get_page(page)
    return render(request, 'product/list.html', {"cards": cards})


def lp(request):
    try:
        s = request.COOKIES["w"]
    except:
        logging.info(request.COOKIES["w"])
        s = None
    if s == "" or s is None:
        message = "Чтото не так"
        return message
    else:
        s = s.encode()
        s = base64.b64decode(s).decode('utf-8')
        s = json.loads(s)
    logging.info(s)
    try:
        r = len(s) - 1
        for k, v in s.items():
            logger.info(f'key={k}, value={v}')
            if k != "orderid":
                for ki, vi in v.items():
                    logger.info(f'key={ki}, value={vi}')


    except:
        logger.info("ror")
    return render(request, "tags/cart.html", {'data': r})


def about(request):
    return render(request, "about/list.html")


def contact(request):
    return render(request, "contact/list.html")
