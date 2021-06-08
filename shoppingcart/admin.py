from django.contrib import admin
from .models import Customer

class CustomerList(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'email', 'home_phone', 'work_phone', 'cell_phone', 'addr_line1','addr_line2', 'addr_line3', 'addr_line4', 'city', 'state', 'postal_code')
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer)

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
