from django.contrib import admin
from .models import Tag


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', "slug", 'active']

    class Meta:
        model = Tag


admin.site.register(Tag, ProductAdmin)
