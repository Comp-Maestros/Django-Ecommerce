from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#admin kiash Ecom Shop
admin.site.site_header='Admin  Ecom Shop'
admin.site.site_title='Admin Ecom Shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('',include('core.urls',namespace='core')),
    path('checkout/',include('checkout.urls',namespace='checkout')),
    path('aboutus/',include('aboutus.urls',namespace='aboutus')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('contact/',include('contact.urls',namespace='contact')),   
    path('mycart/',include('mycart.urls',namespace='mycart')),
    path('products/',include('products.urls',namespace='products')),
    path('knowledge/',include('knowledge.urls',namespace='knowledge'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)