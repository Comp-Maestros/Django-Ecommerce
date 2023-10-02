from django.urls import path
from .views import CheckoutView

app_name='checkout'
urlpatterns=[
    path('',CheckoutView,name='check')
]