from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
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


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
