from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

