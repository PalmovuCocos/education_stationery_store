from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import AddBasketFrom, RegisterUserForm, LoginUserForm
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
    basket_data = Basket.objects.filter(user_id=request.user.pk)
    product = []
    context = {
        'title': 'Корзина',
        'basket': basket_data,
        'product': product,
    }
    return render(request, 'catalog/basket.html', context=context)


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":    # проверка, был ли отправлен запрос
        form = AddBasketFrom(request.POST)
        if form.is_valid():    # проверка на правильность введенных данных
            try:
                Basket.objects.create(product_id=product.pk,
                                      user_id=request.user.pk,
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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'catalog/authorization.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

