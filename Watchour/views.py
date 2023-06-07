from django.shortcuts import render
from store.models import Product
from category.models import Category


def home(request):
    categories = Category.objects.all()[:7]
    selected_category = request.GET.get('category_name', '')

    if selected_category:
        selected_category = Category.objects.get(category_name=selected_category)
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'home.html', context=context)