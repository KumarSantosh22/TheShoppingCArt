# Generated by Django 3.1.7 on 2021-05-08 05:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_auto_20210507_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4),
        ),
    ]
