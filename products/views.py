from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
    }
    return render(request, 'products/products.html', context)
