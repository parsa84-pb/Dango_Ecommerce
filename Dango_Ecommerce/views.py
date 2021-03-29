from django.shortcuts import render
from eshop_products.models import Product
from eshop_products.views import my_grouper
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting
from eshop_product_category.models import ProductCategory
from eshop_order.models import Order


def header(request, *args, **kwargs):
    settings = SiteSetting.objects.first()
    categories = ProductCategory.objects.all()[:8]
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_tracking = Order.objects.filter(owner_id=request.user.id, is_paid=True, is_received=False).all()
    context = {
        'title': 'this title',
        'settings': settings,
        "categories": categories,
        'details': None,
        "order_tracking": None
    }
    if order_tracking.first() is not None:
        context['order_tracking'] = order_tracking
    if open_order is not None:
        context['details'] = open_order.orderdetail_set.all()
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    settings = SiteSetting.objects.first()
    categories = ProductCategory.objects.all()
    context = {
        'settings': settings,
        "categories": my_grouper(6, categories)

    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    slider = Slider.objects.all()
    most_visit_product = Product.object.order_by('-visit_count').all()[:8]
    latest_product = Product.object.order_by('-id').all()[:8]
    categories = ProductCategory.objects.order_by('-id').all()[:10]
    context = {"sliders": slider, "most_visit_product": my_grouper(4, most_visit_product),
               "latest_product": my_grouper(4, latest_product), 'categories': categories}
    return render(request, 'home_page.html', context)

#
# def about_page(request):
#     settings = SiteSetting.objects.first()
#     context = {
#         'settings': settings
#     }
#     return render(request, 'about_page.html', context)
