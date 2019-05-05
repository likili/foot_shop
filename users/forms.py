from django import forms
from users.models import ManagerUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages


class ManagerUserForm(forms.ModelForm):
    class Meta:
        model = ManagerUser

        fields = ['name', 'password']

        # labels = {
        #     'name': u'Логин',
        #     'password': u'Пароль',
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'type': 'password'})
