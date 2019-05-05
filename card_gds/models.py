from django.db import models
from catalog.models import SubCategory
from PIL import Image, ImageEnhance
import random
from django.utils.html import format_html


def make_upload_path(instance, filename, prefix=False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    filename = str(n1) + "_" + str(n2) + "_" + str(n3) + '.jpg'

    return filename


class Cards(models.Model):
    name = models.CharField(verbose_name=u'Наменование товара', max_length=255, help_text="Наменование товара")

    surname = models.TextField(verbose_name=u'Описание товара', null=True, blank=True)
    photo = models.ImageField(blank=True, verbose_name="Изображение", null=True)
    price = models.IntegerField(verbose_name=u'Цена', null=True, blank=True)
    keywords = models.CharField(verbose_name=u'keywords', max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name=u'description', max_length=300, null=True, blank=True)
    best_sales = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Карточка товара'
        verbose_name_plural = u'Карточки товаров'

    def __str__(self):
        return self.name

    photo.short_description = 'Thumb'
    photo.allow_tags = True

    def image_img(self):
        if self.photo:
            return format_html(u'<img src="%s" width="70" />' % self.photo.url)
        else:
            return '(none)'


class CardsComment(models.Model):
    pass


class Partners(models.Model):
    name = models.CharField(verbose_name=u'Наменование бренда', max_length=255, help_text="Наменование бренда")

    surname = models.TextField(verbose_name=u'Описание бренда', null=True, blank=True)
    photo = models.ImageField(blank=True, verbose_name="Изображение", null=True)
    keywords = models.CharField(verbose_name=u'keywords', max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name=u'description', max_length=300, null=True, blank=True)
    trusted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name_plural = u'Партнеры'

    def __str__(self):
        return self.name

    photo.short_description = 'Thumb'
    photo.allow_tags = True

    def image_img(self):
        if self.photo:
            return format_html(u'<img src="%s" width="70" />' % self.photo.url)
        else:
            return '(none)'


class Baners(models.Model):
    name = models.CharField(verbose_name=u'Наменование Акции', max_length=255, help_text="Наменование бренда")

    photo = models.ImageField(blank=True, verbose_name="Изображение", null=True)
    head_1 = models.CharField(verbose_name=u'Заголовок 1', max_length=255)
    head_2 = models.CharField(verbose_name=u'Заголовок 2', max_length=255)
    head_3 = models.CharField(verbose_name=u'Заголовок 3', max_length=255)
    category = models.CharField(verbose_name=u'Заголовок категории', max_length=255)
    link = models.CharField(verbose_name=u'Ссылка на акцию', max_length=255, help_text="Ссылка на акцию")
    cards = models.ManyToManyField(Cards)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'Банер'
        verbose_name_plural = u'Банеры'

    def __str__(self):
        return self.name

    photo.short_description = 'Thumb'
    photo.allow_tags = True

    def image_img(self):
        if self.photo:
            return format_html(u'<img src="%s" width="70" />' % self.photo.url)
        else:
            return '(none)'
