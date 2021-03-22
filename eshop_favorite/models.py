from django.contrib.auth.models import User
from django.db import models

from eshop_products.models import Product


class ProductManager(models.Manager):
    def get_by_id(self, userid):
        return self.get_queryset().filter(owner_id=userid)


class FavoriteProductList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول', null=True)

    object = ProductManager()

    class Meta:
        verbose_name = 'لیست علاقه مندی ها'
        verbose_name_plural = 'لیست های علاقه مندی کاربران'

    def __str__(self):
        return self.user.username
