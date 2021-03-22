import os

from django.db import models


def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.siteTitle}{ext}"
    return f"product/{final_name}"


class SiteSetting(models.Model):
    siteTitle = models.CharField(max_length=300, verbose_name='عنوان سایت')
    siteAddress = models.CharField(max_length=400, verbose_name='آدرس سایت')
    sitePhone = models.IntegerField(max_length=50, verbose_name='تلفن')
    siteMobile = models.IntegerField(max_length=50, verbose_name='تلفن همراه')
    siteEmail = models.EmailField(max_length=150, verbose_name='ایمیل سایت')
    siteFax = models.CharField(max_length=200, verbose_name='فکس سایت')
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.siteTitle
