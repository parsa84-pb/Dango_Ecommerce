from django.urls import path

from eshop_products.views import remove_comment, open_or_close_comment

urlpatterns = [
    path('remove_comment/<pk>', remove_comment),
    path('open_or_close_comment/<pk>', open_or_close_comment),

]
