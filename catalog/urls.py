from django.conf.urls import url
from catalog import views

app_name = 'catalog'
urlpatterns = [
    url(r'^$', views.CatalogListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CatalogDetailView, name='detail'),
    url(r'^categ/(?P<name>\w+)/$', views.subcat, name='categ'),
    
]
