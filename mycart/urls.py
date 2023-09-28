from django.urls import path
from .views import CartView

app_name = 'mycart'

urlpatterns = [
    path('', CartView, name='cart'),
]