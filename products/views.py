from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)
