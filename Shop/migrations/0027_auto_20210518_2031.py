# Generated by Django 3.1.7 on 2021-05-18 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0026_orderlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='date_of_order',
            field=models.DateField(default=datetime.datetime(2021, 5, 18, 15, 1, 57, 714776, tzinfo=utc)),
        ),
    ]