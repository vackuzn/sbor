"""
Django settings for internet_shop project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from .settings_dependencies import is_dev, get_media_root, get_static_root, get_secret_key, get_email_conf, \
    get_allowed_hosts, get_secure_ssl_redirect
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret_key(BASE_DIR)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_dev(BASE_DIR)

CART_SESSION_ID = 'cart'  # Это ключ, который мы собираемся использовать для хранения корзины в сессии пользователя.

ALLOWED_HOSTS = get_allowed_hosts(BASE_DIR)

SECURE_SSL_REDIRECT = get_secure_ssl_redirect(BASE_DIR)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'user_and_customer.apps.UserAndCustomerConfig',
    'cart.apps.CartConfig',
    'order_and_pay.apps.OrderAndPayConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'internet_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'internet_shop', 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_context_processor.cart',
                'main.context_processors.main_context_processor.main'
            ],
        },
    },
]

WSGI_APPLICATION = 'internet_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# Static/media
STATIC_ROOT = get_static_root(BASE_DIR)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'internet_shop/static'),
   os.path.join(BASE_DIR, 'main/static'),
   os.path.join(BASE_DIR, 'user_and_customer/static'),
   os.path.join(BASE_DIR, 'cart/static'),
   os.path.join(BASE_DIR, 'order_and_pay/static'),
]
MEDIA_ROOT = get_media_root(BASE_DIR)
MEDIA_URL = '/media/'

# настройки почтового сервера для отправки писем
email_conf = get_email_conf(BASE_DIR)
EMAIL_HOST = email_conf['EMAIL_HOST']
EMAIL_HOST_USER = email_conf['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_conf['EMAIL_HOST_PASSWORD']
EMAIL_PORT = email_conf['EMAIL_PORT']
EMAIL_USE_SSL = email_conf['EMAIL_USE_SSL']
SEND_EMAIL_TO = email_conf['SEND_EMAIL_TO']
