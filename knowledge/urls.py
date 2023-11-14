from django.urls import path
from .views import Knowldege

app_name='knowledge'

urlpatterns=[
    path('',Knowldege,name='knowledge')
]