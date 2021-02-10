from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('category/', categories, name='categories'),
    path('category/category_<int:id>', category, name='category')
]
