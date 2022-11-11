from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('shop/', Shop.as_view(), name="shop"),
    path('basket/', basket, name="basket"),
    path('shop/product/<int:product_id>/', show_product.as_view(), name='show_product'),
    path('authorization', LoginUser.as_view(), name='authorization'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),

    path('api/v1/products', ProductAPIView.as_view(), name='productAPI')
]
