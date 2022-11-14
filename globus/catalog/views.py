from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView

from rest_framework import generics, viewsets
from rest_framework.views import APIView

from .forms import AddBasketFrom, RegisterUserForm, LoginUserForm
from .models import *
from .serializers import ProductSerializer


class Index(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class Shop(ListView):
    model = Product
    template_name = 'catalog/shop.html'
    context_object_name = 'items'   # переменная в html (иначе object_list)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
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


class Show_product(View):
    form = AddBasketFrom
    initial = {'amount': 'value'}
    template_name = 'catalog/product.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        context = {
            'title': product.name,
            'product': product,
            'form': self.form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = self.form(request.POST)
        context = {
            'title': product.name,
            'product': product,
            'form': form,
        }
        if form.is_valid():
            Basket.objects.create(product_id=product.pk,
                                  user_id=request.user.pk,
                                  amount=form.cleaned_data['amount'])  # запос на добавление корзины
            return redirect('shop')  # редирект на страницу с списком товара
        return render(request, self.template_name, context=context)


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

# 25 минута
class ProductAPIView (generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

