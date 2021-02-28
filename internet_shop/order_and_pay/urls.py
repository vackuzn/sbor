from django.urls import path, include
from order_and_pay.views import *

urlpatterns = [
    path('', order, name='order'),
]