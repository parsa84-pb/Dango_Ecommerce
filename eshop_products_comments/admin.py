from django.contrib import admin
from .models import ProductComment


# Register your models here.

class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', "product", 'text']

    class Meta:
        model = ProductComment


admin.site.register(ProductComment, ProductCommentAdmin)
