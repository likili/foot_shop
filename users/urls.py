from django.conf.urls import url
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.manager_auth, name='list'),
]