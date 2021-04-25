# Generated by Django 3.1.7 on 2021-04-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20210424_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='season',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='year',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
