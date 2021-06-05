from django.contrib import admin

# Model imports
from .models import product

#Admin Classes
class ProductList(admin.ModelAdmin):
    list_display = ('product_name', 'product_description', 'price')
    list_filter = ('product_name', 'price')
    search_fields = ['product_name']
    ordering = ['product_name']


# Model Registers
admin.site.register(product, ProductList)
