from django.contrib import admin
from django.urls import path,include

#admin kiash Ecom Shop
admin.site.site_header='Admin  Ecom Shop'
admin.site.site_title='Admin Ecom Shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    path('aboutus/',include('aboutus.urls',namespace='aboutus'))
]
