from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from main.models import Product
from django.urls import reverse


class Order(models.Model):
    CHOICES_CITY = [
        ('spb', 'Санкт-Петербург'),
        ('psh', 'Пушкин'),
        ('gatchina', 'Гатчина'),
        ('vsecologsk', 'Всеволожск'),
    ]

    CHOICES_STATUS = [
        ('order_is_made', 'Заказ оформлен'),
        ('order_is_paid', 'Заказ оплачен'),
        ('order_is_fulfilled', 'Заказ выполнен'),
    ]

    id = models.AutoField(primary_key=True)
    order_number = models.IntegerField(unique=True, verbose_name='Номер заказа')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='user_order', verbose_name='Пользователь')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    phone = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='Адрес электронной почты')
    address = models.TextField(verbose_name='Адрес')
    city = models.CharField(max_length=200, choices=CHOICES_CITY, default='Saint-Petersburg', verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    total_price = models.IntegerField(verbose_name='Общая цена')
    status = models.CharField(max_length=200, choices=CHOICES_STATUS, default='order_is_made', verbose_name='Статус')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.order_number)

    def get_total_cost(self):
        total_cost = 0
        for order_product in self.OrderProduct.all():
            total_cost += order_product.get_cost()
        return total_cost

    def get_absolute_url(self):
        return reverse('view_order', args=[self.order_number])


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='OrderProduct')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def get_cost(self):
        return int(self.quantity) * float(self.price)

    def __str__(self):
        return str(self.order.order_number) + '_' + str(self.product.title)




