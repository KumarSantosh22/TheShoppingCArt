# Generated by Django 3.1.7 on 2021-05-04 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0003_auto_20210504_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customerid',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='productid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sellerid',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='seller_id',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='type_choice',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='address',
            new_name='residential_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='reg_date',
        ),
        migrations.AddField(
            model_name='customer',
            name='permanent_address',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='residential_address',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
