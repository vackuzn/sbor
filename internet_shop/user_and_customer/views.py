from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages

from user_and_customer.forms import *
from user_and_customer.models import *


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            customer_phone = form.cleaned_data['phone']
            new_user = form.save()
            Customer.objects.create(
                user=new_user,
                phone=customer_phone
            )
            login(request, new_user)
            return redirect('main_page')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'user_and_customer/register.html', context)


def user_login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserAuthenticationForm()
    context = {'form': form}
    return render(request, 'user_and_customer/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('main_page')


def success(request):
    return render(request, 'user_and_customer/success.html')


