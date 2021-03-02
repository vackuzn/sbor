from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from order_and_pay.forms import OrderForm
from order_and_pay.models import Order
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AnonymousUser
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


def make_order(request):
    cart = Cart(request)
    order_number = _get_random_order_number()

    if request.method == "POST":
        form = OrderForm(request.POST)
        # создание и сохранение общего заказа в БД
        if form.is_valid():
            new_order = form.save(commit=False)
            # order number
            new_order.order_number = request.POST.get('order_number')
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
            return HttpResponseRedirect(reverse('pay_order', args=[new_order.order_number]))

    else:
        form = OrderForm()

    context = {'form': form, 'order_number': order_number}
    return render(request, 'order_and_pay/make_order.html', context)


def view_order(request, order_number):
    order = Order.objects.get(order_number=order_number)
    products = order.OrderProduct.all()
    context = {'order': order, 'products': products}
    return render(request, 'order_and_pay/view_order.html', context)


def pay_order(request, order_number):
    order = Order.objects.get(order_number=order_number)
    if request.method == "POST":
        order.status = 'order_is_paid'
        order.save()
        return HttpResponseRedirect(reverse('view_order', args=[order_number]))

    context = {'order': order}
    return render(request, 'order_and_pay/pay.html', context)


def search_order(request):
    if request.method == 'POST':
        if request.POST.get('order_number'):
            orders = Order.objects.filter(order_number=request.POST.get('order_number'))
            context = {'orders': orders}
            return render(request, 'order_and_pay/search_order.html', context)
    return render(request, 'order_and_pay/search_order.html')


def my_order(request):
    if request.user.is_authenticated:
        user = request.user
        orders = user.user_order.all()
        context = {'orders': orders}
        return render(request, 'order_and_pay/my_orders.html', context)
    return HttpResponseRedirect(reverse('login'))