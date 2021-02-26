from django.urls import path, include
from cart.views import *

urlpatterns = [
    path('', cart_page, name='cart'),
    path('cart_dell_product/<int:id>', cart_dell_product, name='cart_dell_product'),

]