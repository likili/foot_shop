from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from basket.models import OrderItems, Order
from django.contrib import messages




class ModelOrderItemsForm(forms.ModelForm):
    
    class Meta:
        model = OrderItems
        fields = ['nameid', 'name', 'category', 'price',
                  'quantity', 'orderid']
        labels = {
            'name': u'Название',
            'count': u'Количество',
            'quantity': u'Сумма',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nameid'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})


class ModelOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['name', 'orderid',
                  'phone', 'city',
                  'adress', 'email'
                   ]
        widgets = {'pay': forms.RadioSelect,
                   'delivery': forms.RadioSelect}
        labels = {
            'name': u'Имя',
            'phone': u'Телефон',
            'city': u'Город',
            'adress': u'Адресс',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})




