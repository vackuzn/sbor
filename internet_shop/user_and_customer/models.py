from django.db import models
from django.contrib.auth import get_user_model


class Customer(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='Покупатель', on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
