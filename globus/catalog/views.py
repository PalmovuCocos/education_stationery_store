from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddBasketFrom
from .models import *


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
    if request.method == "POST":
        form = AddBasketFrom(request.POST)
        if form.is_valid():
            try:
                Basket.objects.create(product_id=product.pk,
                                      user_id=1,
                                      amount=form.cleaned_data['amount'])
                return redirect('shop')
            except:
                form.add_error(None, "Ошибка добавления продукта")
    else:
        form = AddBasketFrom()
    context = {
        'title': product.name,
        'product': product,
        'form': form,
    }
    return render(request, 'catalog/product.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
