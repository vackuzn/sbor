from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', global_categories, name='main_page'),
    path('category/', global_categories, name='global_categories'),
    path('category/<slug>', category, name='category'),
    path('product/<int:pk>', product_card, name='product_card'),
    path('contacts/', contacts, name='contacts'),
    path('wish/', wish, name='wish'),
    path('delivery_terms/', delivery_terms, name='delivery_terms'),
]
