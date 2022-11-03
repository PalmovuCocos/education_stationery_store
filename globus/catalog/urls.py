from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('shop/', Shop.as_view(), name="shop"),
    path('basket/', basket, name="basket"),
    path('shop/product/<int:product_id>/', show_product, name='show_product'),
]
