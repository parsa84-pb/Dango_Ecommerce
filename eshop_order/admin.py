from django.contrib import admin
from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', "is_paid", 'payment_date']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
