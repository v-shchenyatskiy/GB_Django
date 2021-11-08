from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Главная'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        # category = ProductCategory.objects.get(id=category_id)
        # products = Product.objects.filter(category=category)
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
