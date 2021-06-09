from django import forms
from .models import Customer
from .models import Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'addr_line1')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'price')
