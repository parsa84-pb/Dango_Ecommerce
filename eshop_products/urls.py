from django.urls import path

from .views import ProductsList, product_detail, SearchProductsView, ProductsListByCategory, product_categories_partial

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<pk>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products_categories_partial', product_categories_partial, name='product_categories_partial'),
]
