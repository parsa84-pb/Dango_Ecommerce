# Generated by Django 3.1.1 on 2020-12-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0007_remove_product_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید ها'),
        ),
    ]
