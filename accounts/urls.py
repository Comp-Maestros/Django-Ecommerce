from django.urls import path    
from .views import RegisterView,LoginView

app_name='accounts'

urlpatterns=[
    path('',RegisterView,name='register'),
    path('login/',LoginView,name='login'),
]