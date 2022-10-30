from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('shop/', shop, name="shop"),
    path('basket/', basket, name="basket"),
]
