import os
from django.db import models
from PIL import Image


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{instance.title}{ext}"
    return f"sliders/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(verbose_name='آدرس')
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self
        width, height = 490, 445
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(self.image.path, optimize=True, quality=100)
