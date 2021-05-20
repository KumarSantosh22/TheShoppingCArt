from django.db import models
import django.utils.timezone

# Create your models here.


class Transaction(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    order_id = models.CharField(max_length=25)
    payment_id = models.CharField(max_length=25)
    sign = models.TextField(max_length=100)
    pay_date = models.DateTimeField(default=django.utils.timezone.now)
