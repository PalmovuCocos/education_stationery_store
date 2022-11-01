from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'name']


class Basket(models.Model):
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    basket = models.ForeignKey("Basket", on_delete=models.PROTECT)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

