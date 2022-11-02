from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def index(request):    # httpRequest
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'catalog/index.html', context=context)


def shop(request):
    items = Product.objects.all()
    context = {
        'title': 'Каталог',
        'items': items,
    }
    return render(request, 'catalog/shop.html', context=context)


def basket(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'catalog/basket.html', context=context)


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'title': product.name,
        'product': product
    }
    return render(request, 'catalog/product.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
