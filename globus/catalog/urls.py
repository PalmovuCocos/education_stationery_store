from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('shop/', Shop.as_view(), name="shop"),
    path('basket/', BasketShow.as_view(), name="basket"),
    path('shop/product/<int:product_id>/', Show_product.as_view(), name='show_product'),
    path('authorization', LoginUser.as_view(), name='authorization'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile', OrderList.as_view(), name='profile'),

    path('api/v1/products', ProductAPIView.as_view(), name='productAPI')
]
