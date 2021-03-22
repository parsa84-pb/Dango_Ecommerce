from django.db import models


# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمل')
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    is_read = models.BooleanField(verbose_name='خوانده شده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'پیام های کاربران'

    def __str__(self):
        return self.name
