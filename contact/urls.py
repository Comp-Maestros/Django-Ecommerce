from django.urls import path
from .views import ConatactView

app_name='contact'

urlpatterns=[
    path('',ConatactView,name='contact')
]