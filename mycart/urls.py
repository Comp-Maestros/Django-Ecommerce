from django.urls import path
from .views import CartView,Shopping

app_name = 'cart'

urlpatterns = [
    path('', CartView, name='cart'),
    path('shop/',Shopping,name='shop')
]