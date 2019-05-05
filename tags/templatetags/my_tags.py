from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, cookie
from http import cookies
import uuid
import time
import os
import sys
import base64
import json
import cgi
register = template.Library()

from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Snipet
# верхний регистр

def my_app_name(app_name):
    try:
        app = __import__(app_name.lower())
        return app.app_label
    except:
        return app_name

my_app_name = register.simple_tag(my_app_name)

@register.filter
def lang(value):
    value=str(value)
    parts= value.split("/")
    return "/".join(parts[2:])

@register.filter
def fw(value):
    value= unicode(value)
    parts= value.split(" ")
    n = "<span>" + parts[0] + "</span>"
    a = " ".join(parts[1:])
    return n + a

@register.inclusion_tag("tags/top_menu.html")
def top_menu():
    from catalog.models import MenuItem, Menu
    menu = Menu.objects.get(pk=1)
    items = MenuItem.objects.filter(menu=menu, published=1).order_by("ordering")
    return {'items': items}



@register.inclusion_tag("tags/snip.html")
def snip(id):
    data = get_object_or_404(Snipet, pk=int(id))
    return {'data':data}

@register.inclusion_tag("tags/cart.html")
def cart():
    try:
        s = cookie.SimpleCookie(os.environ.get("HTTP_COOKIE"))
        s = s.get("w").value
    except:
        print(cookies.SimpleCookie(os.environ.get("HTTP_COOKIE")))
        s = None
    if s == "" or s is None:
        message = "Чтото не так"
        return message
    else:
        s = s.encode()
        s = base64.b64decode(s).decode('utf-8')
        s = json.loads(s)
    print(s)
    try:
        r = len(s) - 1
        if r > 0:
            data = s
        else:
            data = 0
        #
        # for k, v in s.items():
        #     print(f'key={k}, value={v}')
        #     if k != "orderid":
        #         for ki, vi in v.items():
        #             print(f'key={ki}, value={vi}')

        # qs = super().get(request, *args, **kwargs)
    except:
        print("ror")
    return {'data': data}

@register.simple_tag
def myuerls():
    params = os.getenv("QUERY_STRING") #cgi.FieldStorage()
    name = params
    return name
