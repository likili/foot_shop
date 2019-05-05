"""food_shop_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url #, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# from food_shop_new import settings
from catalog.views import index, lp, about, contact
from django.conf import settings
# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include('card_gds.urls', namespace='cards')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('users/', include('users.urls', namespace='users')),
    url(r'^$', index, name='index'),
    url(r'^lp/$', lp, name='lp'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('api/v1/chat/', include("chat_room.urls", namespace='chat')),

    # адреса для авторизации djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # url(r'^__debug__/', include(debug_toolbar.urls)),
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
