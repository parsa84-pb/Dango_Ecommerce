from django.urls import path

from eshop_order.views import add_user_order, user_open_order, remove_order_detail, \
    order_detail_count_down, order_detail_count_up, add_user_order_product_list

urlpatterns = [
    path('add-user-order', add_user_order),
    path('add-user-order-product-list/<pk>', add_user_order_product_list),
    path('open_order', user_open_order),
    path('remove_order_detail/<detail_id>', remove_order_detail),
    path('order_detail_count_up/<detail_id>', order_detail_count_up),
    path('order_detail_count_down/<detail_id>', order_detail_count_down),
    # path('request', send_request, name='request'),
    # path('verify/<order_id>', verify, name='verify'),
]
