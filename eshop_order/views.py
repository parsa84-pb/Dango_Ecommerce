import time
from functools import lru_cache
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from eshop_products.models import Product
from .forms import UserNewOrderForm, UserInfo, ShowUserInfo
from .models import Order, OrderDetail
from django.http import HttpResponse
from zeep import Client


@login_required(login_url='/login')
@lru_cache
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data['product_id']
        count = new_order_form.cleaned_data['count']
        product = Product.object.filter(id=product_id).first()
        order_detail = order.orderdetail_set.filter(product_id=product_id).first()
        if order_detail is None:
            order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        elif order_detail is not None:
            order_detail.count = count
            order_detail.save()

    return redirect('/open_order')


@login_required(login_url='/login')
@lru_cache
def add_user_order_product_list(request, *args, **kwargs):
    if request.user.is_authenticated:
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = kwargs['pk']
        count = 1
        product = Product.object.filter(id=product_id).first()
        order_detail = order.orderdetail_set.filter(product_id=product_id).first()
        if order_detail is None:
            order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        elif order_detail is not None:
            order_detail.count = count
            order_detail.save()

    return redirect('/open_order')


@login_required(login_url='/login')
@lru_cache
def user_open_order(request):
    context = {
        'order': None,
        'details': None,
        'total_product': 0,
        "form": None
    }
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        user_info = UserInfo(request.POST or None,
                             initial={'full_name': open_order.user_fullname, 'number': open_order.user_number,
                                      "address": open_order.user_address, "postal_code": open_order.user_postal_code})
        if user_info.is_valid():
            full_name = user_info.cleaned_data["full_name"]
            number = user_info.cleaned_data["number"]
            address = user_info.cleaned_data["address"]
            postal_code = user_info.cleaned_data["postal_code"]
            open_order.user_fullname = full_name
            open_order.user_number = number
            open_order.user_address = address
            open_order.user_postal_code = postal_code
            open_order.save()
            return redirect('/confirm_order')

        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total_product'] = open_order.get_total_price()
        context['total'] = context["total_product"] + 10000
        context['form'] = user_info
    return render(request, 'order/user_open_order.html', context)


@login_required(login_url='/login')
@lru_cache
def confirm_order(request):
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order.orderdetail_set.count() == 0:
        return redirect('/open_order')
    user_info = ShowUserInfo(request.POST or None,
                             initial={'full_name': open_order.user_fullname, 'number': open_order.user_number,
                                      "address": open_order.user_address, "postal_code": open_order.user_postal_code})
    return render(request, 'order/confirm_order.html',
                  {"form": user_info, "total_product": open_order.get_total_price(),
                   "total": open_order.get_total_price() + 10000})


@login_required(login_url='/login')
@lru_cache
def order_tracking(request, *args, **kwargs):
    ref_id = kwargs['ref_id']
    order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=True, is_received=False,
                                        ref_id=ref_id).first()
    if order is None:
        return redirect('/open_order')

    context = {'order': order, 'details': order.orderdetail_set.all()}
    return render(request, 'order/order_tracking.html', context)


@login_required(login_url='/login')
@lru_cache
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
    return redirect('/open_order')


@lru_cache
def order_detail_count_up(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.count += 1
            order_detail.save()
    return redirect('/open_order')


@lru_cache
def order_detail_count_down(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            if order_detail.count > 1:
                order_detail.count -= 1
                order_detail.save()
    return redirect('/open_order')


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/verify/'  # Important: need to edit for realy server.


def send_request(request, *args, **kwargs):
    amount = 0
    open_order: Order = Order.objects.filter(is_paid=False, owner_id=request.user.id).first()
    if open_order is not None:
        amount = open_order.get_total_price()
        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile,
                                               f"{CallbackURL}{open_order.id}")
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


def verify(request, *args, **kwargs):
    order_id = kwargs.get('order_id')
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_order = Order.objects.get_queryset().get(id=order_id)
            user_order.is_paid = True
            user_order.payment_date = time.time()
            user_order.ref_id = str(result.RefID)
            user_order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
