from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import AddBasketFrom, RegisterUserForm
from .models import *


class Index(View):

    def get(self, request):
        context = {
            'title': 'Главная страница',
        }
        return render(request, 'catalog/index.html', context=context)


class Shop(ListView):
    model = Product    # определение выводимых записей таблицы бд
    # определение, какая будет открываться html страница (по умолчанию, если не указывать, catalog/Product_list.html)
    template_name = 'catalog/shop.html'
    # указание нзвания переменной для передачи записей из бд и использования в html (если не указывать, то object_list)
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


def basket(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'catalog/basket.html', context=context)


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":    # проверка, был ли отправлен запрос
        form = AddBasketFrom(request.POST)
        if form.is_valid():    # проверка на правильность введенных данных
            try:
                Basket.objects.create(product_id=product.pk,
                                      user_id=1,
                                      amount=form.cleaned_data['amount'])    # запос на добавление корзины
                return redirect('shop')    # редирект на страницу с списком товара
            except:
                form.add_error(None, "Ошибка добавления продукта")
    else:    # если запрос не отправлен, то формируется форма
        form = AddBasketFrom()
    context = {
        'title': product.name,
        'product': product,
        'form': form,
    }
    return render(request, 'catalog/product.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


def authorization(request):
    return HttpResponseNotFound('Авторизация')
