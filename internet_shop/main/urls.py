from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', global_categories, name='main_page'),
    path('global_category/', global_categories, name='global_categories'),
    path('global_category/<slug>', global_category, name='global_category'),
    path('category/<slug>', category, name='category'),
    path('product/<int:pk>', product_card, name='product_card')
]
