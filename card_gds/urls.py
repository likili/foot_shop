from django.conf.urls import url
from card_gds import views
from basket.views import bascet_card_add

app_name = 'cards'
urlpatterns = [
    url(r'^$', views.CardsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CardsDetailView.as_view(), name='detail'),
    url(r'basket/$', bascet_card_add, name='basket'),
]
