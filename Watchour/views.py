from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    categories = Category.objects.all()[:7]

    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html', context=context)
