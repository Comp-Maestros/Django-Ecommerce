from django.urls import path
from .views import AboutView

app_name='aboutus'


urlpatterns=[
    path('',AboutView,name='aboutus')
]