from django.db import models


class ManagerUser(models.Model):
    name = models.CharField(verbose_name=u'Логин', max_length=255, help_text="Логин")
    password = models.CharField(verbose_name=u'Пароль', max_length=255, help_text="Пароль")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Менеджер'
        verbose_name_plural = u'Менеджеры'