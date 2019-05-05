from django.db import models
from card_gds.models import Cards
from catalog.models import SubCategory



class BasketStatus(models.Model):
    name = models.CharField(verbose_name=u'Наменование статусa', max_length=255, help_text="Наменование статусa",
                            null=True, blank=True)
    surname = models.CharField(verbose_name=u'Наменование статусa', max_length=255, help_text="Наменование статусa",
                               null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'Статус заказа'
        verbose_name_plural = u'Статусы заказов'

    def __str__(self):
        return self.name


class OrderItems(models.Model):
    nameid = models.IntegerField(verbose_name=u'ID', null=True, blank=True)
    name = models.CharField(verbose_name=u'Наменование товара', max_length=255, help_text="Наменование товара",
                            null=True, blank=True)
    category = models.CharField(verbose_name=u'Категория', max_length=255, help_text="Категория", null=True, blank=True)
    price = models.IntegerField(verbose_name=u'Ценна', null=True, blank=True)
    quantity = models.IntegerField(verbose_name=u'Сумма', null=True, blank=True)
    orderid = models.CharField(verbose_name=u'odrerID', max_length=255, help_text="Наменование товара", null=True,
                               blank=True)
    status = models.ForeignKey(BasketStatus, on_delete=models.CASCADE, default=1, null=True, blank=True)


class Order(models.Model):
    name = models.CharField(verbose_name=u'Имя заказчика', max_length=255, help_text="Имя заказчика", null=True,
                            blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=15, null=True, blank=True)
    city = models.CharField(verbose_name=u'Город заказчика', max_length=255, help_text="Город заказчика", null=True,
                            blank=True)
    adress = models.CharField(verbose_name=u'Адрес заказчика', max_length=255, help_text="Адрес заказчика", null=True,
                              blank=True)
    orderid = models.CharField(verbose_name=u'Номер корзины', max_length=255, help_text="Номер корзины", unique=True)

    email = models.EmailField(verbose_name=u'Електронная почта', unique=False, null=True)
    pay = models.CharField(max_length=15,
                           choices=(('cash', 'Наличными при получении'),
                                    ('cards', 'Картой при получении'),
                                    ('cred_cards', 'Картой онлайн')),
                           default="cash")
    delivery = models.CharField(max_length=15,
                                choices=(('courier', 'Курьером'),
                                         ('independently', 'Самовывоз')),
                                default="courier")
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(BasketStatus, on_delete=models.CASCADE, default=1)
    print(date_apply)

    class Meta:
        verbose_name = u'Карточка корзины'
        verbose_name_plural = u'Карточки корзины'

    def __str__(self):
        return self.orderid
