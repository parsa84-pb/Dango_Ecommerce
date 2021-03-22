from django.urls import path

from eshop_products.views import remove_comment

urlpatterns = [
    path('remove_comment/<pk>', remove_comment),

]
