import itertools
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from eshop_product_category.models import ProductCategory
from eshop_products_comments.models import ProductComment
from eshop_products_comments.forms import UserNewCommentForm


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 9

    def get_queryset(self):
        return Product.object.filter(active=True)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    product_id = kwargs['pk']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': product_id})
    new_comment = UserNewCommentForm(request.POST or None)
    product = get_object_or_404(Product, pk=product_id)
    comments = ProductComment.objects.filter(product_id=product_id)
    # paginator = Paginator(comments, 1)
    if product.active:
        product.visit_count += 1
        product.save()
        galleries = ProductGallery.objects.filter(product_id=product_id)
        suggestion_products = Product.object.get_queryset().filter(categories__product=product).distinct()[:6]
        page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        context = {'product': product, 'galleries': list(my_grouper(3, galleries)),
                   'suggestion_products': list(my_grouper(3, suggestion_products)), 'new_order_form': new_order_form,
                   'new_comment': None, 'comments': comments}
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            if new_comment.is_valid():
                text = new_comment.cleaned_data.get('text')
                new_product_comment = ProductComment.objects.create(text=text, product=product, user=user)
                new_product_comment.save()
                return redirect(f"/products/{product.id}/{product.title.replace(' ', '-')}")
                # new_comment = UserNewCommentForm()
            context['new_comment'] = new_comment
        return render(request, 'products/product_detail.html', context)
    raise Http404


class SearchProductsView(ListView):
    template_name = "products/products_list.html"
    paginate_by = 9

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.object.search(query)
        return Product.object.filter(active=True)


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 9

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        products = Product.object.get_by_category(category_name).first()
        if products is None:
            raise Http404('دسته بندی مورد نظر یافت نشد')
        return Product.object.get_by_category(category_name)


def product_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'products/products_categories_partial.html', context)


def remove_comment(request, **kwargs):
    if request.user.is_superuser:
        comment_id = kwargs['pk']
        comment = ProductComment.objects.get_queryset().get(id=comment_id)
        comment.delete()
        return redirect(f"/products/{comment.product.id}/{comment.product.title.replace(' ', '-')}")
