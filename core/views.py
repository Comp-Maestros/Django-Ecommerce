from django.shortcuts import render
from products.models import Item
# Create your views here.
def HomeView(request):
    items=Item.objects.all()
    context={
        'items':items
    }
    
    return render(request,'index.html',context)