# furniture/admin.py

from django.contrib import admin
from .models import Furniture, Customer, Supplier

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['furniture_name', 'furniture_type', 'price', 'material_used']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customername', 'cphone', 'cemail']
    filter_horizontal = ('purchase',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['suppler_name', 'sphone', 'semail']
    filter_horizontal = ('supply',)
