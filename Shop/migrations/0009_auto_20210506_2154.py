# Generated by Django 3.1.7 on 2021-05-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20210506_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='image',
            field=models.ImageField(blank=True, default='profile/def_user.png', upload_to='profile/'),
        ),
    ]
