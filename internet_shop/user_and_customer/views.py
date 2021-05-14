from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages

from internet_shop.settings import EMAIL_HOST_USER, SEND_EMAIL_TO
from django.core.mail import send_mail

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
                phone=customer_phone)

            # отправка письма о регисрации нового пользователя владельцу сайта
            subject = 'Новый пользователь {}'.format(str(new_user.username))
            message = 'Зарегистрировался новый пользователь: \nИмя: {}, \nEmail: {}., \nТелефон: {}'.format(str(new_user.username),
                                                                           str(new_user.email),
                                                                           str(customer_phone),
                                                                           )
            send_mail(subject, message, EMAIL_HOST_USER, [SEND_EMAIL_TO], fail_silently=False)

            # отправка письма пользователю
            subject = 'Вы успешно зарегистрировались на сайте https://sbor-market.ru'
            message = '{}, спасибо за регистрацию на сайте https://sbor-market.ru'.format(str(new_user.username))
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email], fail_silently=False)

            # вход на сайт
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


