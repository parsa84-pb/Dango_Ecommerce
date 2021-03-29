from django.contrib import admin
from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', "is_paid", 'is_checking', 'is_posted', 'is_received', 'payment_date']
    list_filter = ['is_checking', 'is_posted', 'is_received']
    list_editable = ['is_checking', 'is_posted', 'is_received']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
