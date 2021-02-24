from django.urls import path, include
from user_and_customer.views import *


urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('success/', success, name='success'),
]
