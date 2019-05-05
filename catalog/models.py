from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image, ImageEnhance
from django.utils.html import format_html


class Category(models.Model):
    name = models.CharField(verbose_name=u'Наменование категории', max_length=255, help_text="Наменование товара", default="vasya")
    slug = models.CharField(verbose_name=u'Url:', max_length=255, null=True, blank=True)
    surname = models.CharField(verbose_name=u'Описание категории', max_length=255, null=True, blank=True)
    indexsurname = models.CharField(verbose_name=u'Описание для главной', max_length=255, null=True, blank=True)
    keywords = models.CharField(verbose_name=u'keywords', max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name=u'description', max_length=300, null=True, blank=True)
    photo = models.ImageField(blank=True, verbose_name="Изображение", null=True)
    is_index = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __str__(self):
        return self.name

    photo.short_description = 'Thumb'
    photo.allow_tags = True

    def image_img(self):
        if self.photo:
            return format_html(u'<img src="%s" width="70" />' % self.photo.url)
        else:
            return '(none)'


class SubCategory(models.Model):
    name = models.CharField(verbose_name=u'Наменование подкатегории', max_length=255, help_text="Наменование товара", default="vasya")
    surname = models.CharField(verbose_name=u'Описание подкатегории', max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  null=True, blank=True)
    photo = models.ImageField(blank=True, verbose_name="Изображение", null=True)
    is_base = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Податегория'
        verbose_name_plural = u'Податегории'

    def __str__(self):
        return self.name

    photo.short_description = 'Thumb'
    photo.allow_tags = True

    def image_img(self):
        if self.photo:
            return format_html(u'<img src="%s" width="70" />' % self.photo.url)
        else:
            return '(none)'

class Menu(models.Model):
    name = models.CharField(verbose_name=u'Название:', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Меню"

class MenuItem(MPTTModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Меню")
    name = models.CharField(verbose_name=u'Название:', max_length=255, default="vasya")
    slug = models.CharField(verbose_name=u'Url:', max_length=255, null=True, blank=True)
    full_text = models.TextField(verbose_name="Полное описаание:", blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, verbose_name=u'Родительский пункт меню:', null=True, blank=True, related_name='children')
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Пункты меню"

    class MPTTMeta:
        order_insertion_by = ['name']


class Snipet(models.Model):
    name = models.CharField(verbose_name=u'Название:', max_length=255, default="vasya")
    text = models.TextField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликовано", default=0)
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Снипеты"
        verbose_name = "Снипет"






