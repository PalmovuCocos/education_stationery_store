from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    category = models.CharField(max_length=20, verbose_name='Категория')
    brand = models.CharField(max_length=20, verbose_name='Бренд')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity_in_stock = models.PositiveIntegerField(verbose_name='Количество на складе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'name']


class Basket(models.Model):
    product = models.ForeignKey("Product", on_delete=models.PROTECT, verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    amount = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['user', 'product']


class Order(models.Model):
    basket = models.ForeignKey("Basket", on_delete=models.PROTECT, verbose_name='Корзина')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Полная цена')
    status = models.CharField(max_length=20, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['basket', 'status']

