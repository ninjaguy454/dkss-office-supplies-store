from django.contrib import admin
from .models import Customer
from .models import Product


class CustomerList(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'home_phone', 'work_phone', 'cell_phone', 'addr_line1', 'addr_line2',
        'addr_line3', 'addr_line4', 'city', 'state', 'postal_code')
    list_filter = ('first_name', 'last_name')
    search_fields = ['first_name']
    ordering = ['first_name']


admin.site.register(Customer, CustomerList)


class ProductList(admin.ModelAdmin):
    list_display = ('product_name', 'product_description', 'price')
    list_filter = ('product_name', 'price')
    search_fields = ['product_name']
    ordering = ['product_name']


# Model Registers
admin.site.register(Product, ProductList)
