# Generated by Django 3.1.1 on 2021-03-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0002_order_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_checking',
            field=models.BooleanField(default=False, verbose_name='بررسی توسط فروشنده'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_posted',
            field=models.BooleanField(default=False, verbose_name='تحویل داده شده به پست'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_received',
            field=models.BooleanField(default=False, verbose_name='دریافت کالا توسط مشتری'),
        ),
    ]
