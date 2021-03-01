from django import forms
from order_and_pay.models import Order


class OrderForm(forms.ModelForm):
    CHOICES_CITY = [
        ('spb', 'Saint-Petersburg'),
        ('psh', 'Pushkin'),
    ]

    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form_field'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form_field'}))
    phone = forms.IntegerField(label='Телефон', widget=forms.NumberInput(attrs={'class': 'form_field'}))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form_field'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'form_field'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'email',  'city', 'address',)
