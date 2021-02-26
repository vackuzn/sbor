from django.shortcuts import render, redirect
from cart.cart import Cart
from main.models import Product


def cart_page(request):
    return render(request, 'cart/cart.html')


def cart_dell_product(request, id):
    product = Product.objects.get(id=id)

    cart = Cart(request)
    cart.remove(product)

    return redirect('cart')