from django.contrib import admin

from .models import Maker, Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Maker)
admin.site.register(Product)
