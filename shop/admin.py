from django.contrib import admin
from .models import Product, Category, Contact


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
