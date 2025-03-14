from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=130, verbose_name='عنوان')
    name = models.CharField(max_length=130, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصولات'

    def __str__(self):
        return self.title
