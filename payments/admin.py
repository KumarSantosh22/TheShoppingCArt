from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'payment_id','user', 'email', 'sign', 'pay_date']
