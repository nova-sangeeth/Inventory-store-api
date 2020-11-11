from django.contrib import admin
# Register your models here.

from .models import Product, Batch, Order


admin.site.register(Product)
admin.site.register(Batch)
admin.site.register(Order)


