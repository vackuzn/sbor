from django import forms


class CartAddProductForm(forms.Form):
    id_product = forms.IntegerField(label='id продукта', widget=forms.HiddenInput)
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'cart_quantity'}))
