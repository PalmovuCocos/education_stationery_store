from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'photo', 'price', 'quantity_in_stock') # поля которые стоит прописать
    list_display_links = ('id', 'name')    # поля через которые можно перейти к записи на сайте
    search_fields = ('name', 'brand')    # по каким полям можно производить поиск информации
    list_editable = ('price', 'quantity_in_stock')    # атрибуты для быстрого редактирования
    list_filter = ('brand',)    # атрибуты по которым можно проводить фильтрацию


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
admin.site.register(Order)


