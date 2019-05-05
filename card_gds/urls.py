from django.conf.urls import url
from card_gds import views
from basket.views import bascet_card_add
from django.views.decorators.cache import cache_page

app_name = 'cards'
urlpatterns = [
    url(r'^$', cache_page(60 * 15)(views.CardsListView.as_view()), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CardsDetailView.as_view(), name='detail'),
    url(r'basket/$', bascet_card_add, name='basket'),
]
