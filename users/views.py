from django.shortcuts import render, redirect
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from users.forms import ManagerUserForm
from users.models import ManagerUser
import logging

logger = logging.getLogger(__name__)



def auther(request):
    if request.POST and ("auth" not in request.session):
        messages.success(request, "Пользователь не загистрирован!")
        logger.info("пользователь не загистрирован")
    elif request.POST and (request.session["auth"] == False):
        logger.info("войти в личный кабинет")
    elif request.POST and (request.session["auth"] == True):
        logger.info("LogOut")

# Пока ручками генерируем пароль для пользователей
# hash = generate_password_hash("password")


def manager_auth(request):
    manager_user = ManagerUser
    if request.method == "POST":
        form = ManagerUserForm(request.POST)
        if form.is_valid():
            manager = form.clean()
            name = manager.get("name")
            pwd = manager.get("password")
            try:
                if ManagerUser.objects.get(name=name) and check_password_hash(ManagerUser.objects.get(name=name).password, pwd):
                    messages.success(request, "Пользователь загистрирован!")
                    request.session['auth'] = True
                    return redirect('basket:admin')
                else:
                    messages.success(request, "Пользователь не загистрирован!")
            except:
                messages.success(request, "Пользователь не загистрирован!")
            return redirect('users:list')
    else:
        form = ManagerUserForm()
    return render(request, 'users/forms/apply.html', {'form': form})
