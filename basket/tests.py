from django.test import TestCase
from basket.models import BasketStatus, OrderItems, Order
from basket.models import OrderItems


class BasketModelTest(TestCase):
    def status_create(self):

        status = BasketStatus.objects.create(
            name="На рассмотрении",
            surname="Не проверенно менеджером",
            is_active=False
        )


    def test_status_create(self):
        self.status_create()
        self.assertEqual(BasketStatus.objects.all().count(), 1)

    def orderitems_create(self):
        orderitems = OrderItems.objects.create(
            orderid='50c612fe-b948-4819-bdbb-ff6ba2b7a58d',
            nameid=555,
            name="Наменование товара",
            category='Категория',
            price=25,
            quantity=30,
            status=None,
        )

    def test_orderitems_create(self):
        self.orderitems_create()
        self.assertEqual(OrderItems.objects.all().count(), 1)

    def order_create(self):
        self.status_create()
        order = Order.objects.create(
            name="Иван",
            phone="8888888",
            city="Москва",
            adress="Красная площадь",
            orderid="50c612fe-b948-4819-bdbb-ff6ba2b7a58d",
            email="moi@mail.ru",
            pay="cash",
            delivery="courier",
            status=BasketStatus.objects.get(id=1),
        )

    def test_order_create(self):
        self.order_create()
        self.assertEqual(Order.objects.all().count(), 1)


