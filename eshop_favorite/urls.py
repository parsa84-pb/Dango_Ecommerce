from django.urls import path
from .views import update_favorite_product_list
from .views import favorite_product_list, remove_favorite_product

urlpatterns = [
    path('favorite_product_list/', favorite_product_list),
    path('remove_favorite_product/<favorite_id>', remove_favorite_product),
    path('update_favorite_product_list/<pk>', update_favorite_product_list),
]