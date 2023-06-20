
from django.contrib import messages
# import Levenshtein
from orders.models import OrderProduct
from store.forms import ReviewForm
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q

from store.models import Product, ReviewRating
from carts.models import Cart, CartItem
from category.models import Category
from carts.views import _cart_id


def store(request, category_slug=None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(products, 15)
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context=context)


def product_detail(request, category_slug, product_slug=None):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        cart = Cart.objects.get(cart_id=_cart_id(request=request))
        in_cart = CartItem.objects.filter(
            cart=cart,
            product=single_product
        ).exists()
    except Exception as e:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )

    try:
        orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
    except Exception:
        orderproduct = None

    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        'single_product': single_product,
        'in_cart': in_cart if 'in_cart' in locals() else False,
        'orderproduct': orderproduct,
        'reviews': reviews,
    }
    return render(request, 'store/product_detail.html', context=context)

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request

    products = Product.objects.filter(Q(product_name__icontains=query))

    context = {
        'products': products,
        'q': query,
        'product_count': products.count()
    }
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    title = 'Watchour - Submit Review'
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Cảm ơn bạn đã đánh giá")
            return redirect(url)
        except:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Cảm ơn bạn đã đánh giá")
                return redirect(url)