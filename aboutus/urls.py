from django.urls import path
from .views import AboutView

app_name='about'
url_patterns=[
    path('',AboutView,name='about')
]