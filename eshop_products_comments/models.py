from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from eshop_products.models import Product


class ProductComment(models.Model):
    text = RichTextField(verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    date = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ")

    class Meta:
        verbose_name = 'نظر کاربر'
        verbose_name_plural = 'نظرات کاربران'

    def __str__(self):
        return self.user.username
