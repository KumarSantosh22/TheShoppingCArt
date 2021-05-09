from django.contrib import admin
from .models import Seller, Customer, Product, Order


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'phone', 'dob', 'gstin', 'category', 'subcategory', 'description', 'residential_address','permanent_address', 'shop_address']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'phone', 'dob', 'residential_address',
                    'permanent_address', 'delievery_address']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','product_id', 'seller', 'price', 'is_discount','discount', 'description', 'image',
                    'category', 'subcategory', 'stock_qty', 'in_stock', 'reorder_qty', 'year', 'type_choice']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderid']

