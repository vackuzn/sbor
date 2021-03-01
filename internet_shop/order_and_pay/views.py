from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from order_and_pay.forms import OrderForm
from order_and_pay.models import Order
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from cart.cart import Cart
from order_and_pay.models import OrderProduct

import random


def _send_email(order_number, total_price, first_name, last_name, address):
    pass


def _get_random_order_number():
    while True:
        order_number = random.randint(1000, 9000000)
        if len(Order.objects.filter(order_number=order_number)) == 0:
            break
    return order_number


def order(request):
    cart = Cart(request)
    order_number = _get_random_order_number()

    if request.method == "POST":
        form = OrderForm(request.POST)
        # создание и сохранение общего заказа в БД
        if form.is_valid():
            new_order = form.save(commit=False)
            # номер заказа
            new_order.order_number = order_number
            # user
            if request.user != AnonymousUser():
                new_order.user = request.user
            # total price
            new_order.total_price = cart.get_total_price()
            # сохранение заказа в БД
            new_order.save()

            # создание и сохранение в БД элементов заказа (продукты)
            for product in cart:
                OrderProduct.objects.create(
                    order=new_order,
                    product=product['product'],
                    price=product['price'],
                    quantity=product['quantity'],
                )

            cart.clear()
            return HttpResponseRedirect(reverse('main_page'))

    else:
        form = OrderForm()

    context = {'form': form, 'order_number': order_number}
    return render(request, 'order_and_pay/order.html', context)


