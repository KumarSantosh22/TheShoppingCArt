from django.contrib import admin
from .models import Seller, Customer, Product, Order


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'phone', 'dob', 'gstin', 'category', 'subcategory', 'description', 'residential_address','permanent_address', 'shop_address']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'phone', 'dob', 'residential_address',
                    'permanent_address', 'delievery_address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderid']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
