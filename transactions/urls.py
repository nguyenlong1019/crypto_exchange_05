from django.urls import path 
from .views import * 


urlpatterns = [
    path('', index, name='index'),
    path('order/create-buy/', create_buy_view, name='create-buy'),
    path('order/create-sell/', create_sell_view, name='create-sell'),
    path('order/buy/<guid>/', buy_detail_view, name='buy-detail'),
]
