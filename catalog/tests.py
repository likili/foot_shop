from django.test import TestCase
from catalog.models import Category, SubCategory, Menu, MenuItem, Snipet
import os
from food_shop_new.settings import MEDIA_ROOT

class CatalogTest(TestCase):
    def category_create(self):
        category = Category.objects.create(
            name="Мужчины",
            slug="men",
            surname="Мужская обувь",
            indexsurname="Мужская обувь",
            keywords="Мужская обувь",
            description="Мужская обувь",
            photo=os.path.join(MEDIA_ROOT, 'test_cat.jpg'),
            is_index=True,

        )

    def test_category_create(self):
        self.category_create()
        self.assertEqual(Category.objects.all().count(), 1)

    def subcategory_create(self):
        self.category_create()
        subcategory = SubCategory.objects.create(
            name="Ботинки",
            surname="Мужская обувь",
            category=Category.objects.get(name="Мужчины"),
            photo=os.path.join(MEDIA_ROOT, 'test_subcat.jpg'),
            is_base=True,
        )

    def test_subcategory_create(self):
        self.subcategory_create()
        self.assertEqual(SubCategory.objects.all().count(), 1)

    def index_page(self):
        from django.test import Client
        client = Client()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)

        self.subcategory_create()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        # проверяет наличие контента на странице
        self.assertContains(response, "test_cat.jpg")


class CatalogViewTest(CatalogTest):
    def test_index_page(self):
        """ проверка статуса загружаемой страницы и контента"""

        from django.test import Client
        client = Client()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)

        self.subcategory_create()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        # проверяет наличие контента на странице
        self.assertContains(response, "cat.jpg")