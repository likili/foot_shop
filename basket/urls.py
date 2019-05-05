from django.conf.urls import url
from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [
    url(r'^$', views.bascet_user_apply, name='list'),

    url(r'order/$', views.OrderView.as_view(), name='order'),
    url(r'order_rem/(?P<pk>\d+)/$', views.basket_order_apply_delete, name='order_rem'),
    url(r'order_save/$', views.bascet_order_save, name='order_save'),
    url(r'edit/(?P<pk>\d+)/$', views.bascet_user_apply_edit, name='edit'),
    url(r'remove/(?P<pk>\d+)/$', views.bascet_user_apply_delete, name='remove'),
    url(r'card/$', views.bascet_card_apply, name='card_list'),
    url(r'card/edit/(?P<pk>\d+)/$', views.bascet_card_apply_edit, name='card_edit'),
    url(r'card/remove/(?P<pk>\d+)/$', views.bascet_card_apply_delete, name='card_remove'),
    url(r'admin/$', views.basket_card_admin, name='admin'),
    path('articles/<uuid>/', views.basket_card_admin_detail, name='admin_detail'),

]
