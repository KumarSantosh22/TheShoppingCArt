# Generated by Django 3.1.7 on 2021-05-07 07:38

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_auto_20210506_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('1.00'), max_digits=10),
        ),
    ]
