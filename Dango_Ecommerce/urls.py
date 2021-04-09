from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from Dango_Ecommerce import settings
from .views import home_page, header, footer

urlpatterns = [
    path('', home_page),
    # path('about-us', about_page),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('', include('eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_contact.urls')),
    path('', include('eshop_order.urls')),
    path('', include('eshop_favorite.urls')),
    path('', include('eshop_products_comments.urls')),
    path('', include('eshop_chat.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Dango_Ecommerce.views.handler404'
