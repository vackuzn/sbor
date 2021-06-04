from django import forms
from main.models import Wish


class WishForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form_field'}))
    title = forms.CharField(label='Краткое описание', widget=forms.TextInput(attrs={'class': 'form_field'}))
    contacts = forms.CharField(label='Адрес электронной почты либо телефон', widget=forms.TextInput(attrs={'class': 'form_field'}))
    description = forms.CharField(label='Подробное описание', widget=forms.Textarea(attrs={'class': 'form_field', 'rows': 5}))

    class Meta:
        model = Wish
        fields = ('name', 'contacts', 'title', 'description',)
