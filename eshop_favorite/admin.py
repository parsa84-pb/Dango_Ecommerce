from django.contrib import admin
from .models import FavoriteProductList


# Register your models here.

class FavoriteProductListAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = FavoriteProductList


admin.site.register(FavoriteProductList, FavoriteProductListAdmin)

