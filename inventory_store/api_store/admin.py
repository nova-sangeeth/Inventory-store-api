from django.contrib import admin
# Register your models here.

from .models import Product, Batch, Order, sale_details


admin.site.register(Product)
admin.site.register(Batch)
admin.site.register(Order)
admin.site.register(sale_details)


