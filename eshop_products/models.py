import os
from django.db import models
from django.db.models import Q
from PIL import Image
from ckeditor.fields import RichTextField
from eshop_product_category.models import ProductCategory


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/galleries/{final_name}"


# Create your models here.
class ProductManager(models.Manager):
    def get_by_id(self, productid):
        qs = self.get_queryset().filter(id=productid)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = RichTextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, default=None, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید ها')
    is_comment_open = models.BooleanField(default=True, verbose_name="باز بودن نظرات")

    object = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def get_absolute_url2(self):
        return f"/update_favorite_product_list/{self.id}/{self.title.replace(' ', '-')}"

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self
        width, height = 268, 200
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(self.image.path, optimize=True, quality=95)


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self
        width, height = 100, 100
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(self.image.path, optimize=True, quality=100)
