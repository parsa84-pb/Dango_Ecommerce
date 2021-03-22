from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from eshop_products.models import Product
from .models import FavoriteProductList
from django.contrib.auth.decorators import login_required


def favorite_product_list(request, *args, **kwargs):
    if not request.user.is_authenticated:
        redirect('/login')
    context = {
        'favorite_product': None,
        'page_obj': None
    }
    favorite_product = FavoriteProductList.object.filter(user_id=request.user.id).all()
    if favorite_product is not None:
        paginator = Paginator(favorite_product, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['favorite_product'] = favorite_product
        context['page_obj'] = page_obj
        return render(request, 'products/favorite_product_list.html', context)


def update_favorite_product_list(request, **kwargs):
    if not request.user.is_authenticated:
        return redirect('/login')
    product_id = kwargs['pk']
    already_exist= False
    # product = Product.object.filter(id=product_id)
    f_list = FavoriteProductList.object.filter(user_id=request.user.id).all()
    if f_list.first() is None:
        pro_list = FavoriteProductList.object.create(user_id=request.user.id, product_id=product_id)
        pro_list.save()
    for i in f_list:
        if product_id in str(i.product.id):
            already_exist = True
    if not already_exist:
        pro_list = FavoriteProductList.object.create(user_id=request.user.id, product_id=product_id)
        pro_list.save()
    return redirect('/favorite_product_list')


@login_required(login_url='/login')
def remove_favorite_product(request, *args, **kwargs):
    favorite_id = kwargs.get('favorite_id')
    if favorite_id is not None:
        favorite_product = FavoriteProductList.object.get_queryset().get(id=favorite_id, user_id=request.user.id)
        if favorite_product is not None:
            favorite_product.delete()
    return redirect('/favorite_product_list/')
