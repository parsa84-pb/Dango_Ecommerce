# Generated by Django 3.1.1 on 2020-11-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_auto_20201119_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='علاقه مندی ها'),
        ),
    ]
