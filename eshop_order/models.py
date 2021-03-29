from django.db import models
from django.contrib.auth.models import User

from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='صاحب')
    is_paid = models.BooleanField(verbose_name='پرداخت شده')
    is_checking = models.BooleanField(verbose_name="بررسی توسط فروشنده", default=False)
    is_posted = models.BooleanField(verbose_name="تحویل داده شده به پست", default=False)
    is_received = models.BooleanField(verbose_name="دریافت کالا توسط مشتری", default=False)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    ref_id = models.CharField(blank=True, null=True, verbose_name='کد پیگیری', max_length=300)
    user_number = models.IntegerField(blank=True, null=True, verbose_name="شماره مشتری")
    user_address = models.CharField(blank=True, null=True, verbose_name="آدرس مشتری", max_length=1500)
    user_postal_code = models.IntegerField(blank=True, null=True, verbose_name="کد پستی مشتری")
    user_fullname = models.CharField(blank=True, null=True, verbose_name="نام و نام خانوادگی مشتری", max_length=150)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.price * self.count

    class Meta:
        verbose_name = 'جزِئیات سبد خرید'
        verbose_name_plural = 'اطلاعات جزئیات سبد خرید'

    def __str__(self):
        return self.product.title
