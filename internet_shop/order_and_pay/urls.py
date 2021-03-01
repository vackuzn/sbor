from django.urls import path
from order_and_pay.views import *

urlpatterns = [
    path('', order, name='order'),
]
