# Generated by Django 3.1.1 on 2021-03-21 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_products', '0012_auto_20210305_2244'),
        ('eshop_favorite', '0005_auto_20201203_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteproductlist',
            name='list',
        ),
        migrations.RemoveField(
            model_name='favoriteproductlist',
            name='owner',
        ),
        migrations.AddField(
            model_name='favoriteproductlist',
            name='product',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favoriteproductlist',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='کاربر'),
            preserve_default=False,
        ),
    ]
