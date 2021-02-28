from django.db import models
from django.contrib.auth import get_user_model
from main.models import Product


class Order(models.Model):
    order_number = models.IntegerField(unique=True, verbose_name='Номер заказа')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    phone = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField()
    address = models.TextField(verbose_name='Адрес')
    city = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    total_price = models.IntegerField(verbose_name='Общая цена')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.order_number

    def get_total_cost(self):
        total_cost = 0
        for order_product in self.OrderProduct.all():
            total_cost += order_product.get_cost()
        return total_cost


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='OrderProduct')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return int(self.quantity) * float(self.price)

    def __str__(self):
        return str(self.order.order_number) + '_' + str(self.product.title)




