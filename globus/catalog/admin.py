from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'photo', 'price', 'quantity_in_stock') # поля которые стоит прописать
    list_display_links = ('id', 'name')    # поля через которые можно перейти к записи на сайте
    search_fields = ('name', 'brand')    # по каким полям можно производить поиск информации
    list_editable = ('price', 'quantity_in_stock')    # атрибуты для быстрого редактирования
    list_filter = ('brand',)    # атрибуты по которым можно проводить фильтрацию


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'amount')
    list_display_links = ('id',)
    search_fields = ('product', 'user')
    list_filter = ('product', 'user')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'total_cost', 'status')
    list_display_links = ('id',)
    search_fields = ('basket', 'status')
    list_editable = ('status',)
    list_filter = ('basket', 'status')


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)


