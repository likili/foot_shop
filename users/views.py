from django.shortcuts import render, redirect
from django.contrib import messages
from werkzeug.security import generate_password_hash, check_password_hash
from users.forms import ManagerUserForm
from users.models import ManagerUser
import logging

logger = logging.getLogger(__name__)


# Create your views here.


# проверка наличия значения в сессиии
def auther(request):
    if request.POST and ("auth" not in request.session):
        # выводи сообщение пользователь не загистрирован
        messages.success(request, "Пользователь не загистрирован!")
        logger.info("пользователь не загистрирован")
    elif request.POST and (request.session["auth"] == False):
        # войти в личный кабинет
        logger.info("войти в личный кабинет")
    elif request.POST and (request.session["auth"] == True):
        # выйти
        logger.info("LogOut")

# Пока ручками генерируем пароль для пользователей
# hash = generate_password_hash("password")


def manager_auth(request):
    manager_user = ManagerUser
    if request.method == "POST":
        # если пришел пост то инициализируем форму с пост
        form = ManagerUserForm(request.POST)
        # проверяем валидная или не валидная какие ошибки пришли
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
            # messages.success(request, "Saved Edit!")
            return redirect('users:list')
    else:
        form = ManagerUserForm()
    return render(request, 'users/forms/apply.html', {'form': form})

"""

# пример можно добавлять комментарии раз в минуту
def addcomment(request):
    if request.POST and ("auth" not in request.session):
        form = CardsCommentForm(request.POST) # пишу в ковычках така как нет такоей формы
        if form.is_valid():
            comment = form.save(commit=False) #  что такое commit
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            # время жизни кук в секундах
            request.session.set_expiry(60)
            # тут мы записываем в сессию которая храниться на компьютере знаение True доступа к сессии нет
            request.session['pause'] = True
        return redirect('adres')


"""