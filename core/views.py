from django.shortcuts import render
from products.models import Item,Popular
# Create your views here.
def HomeView(request):
    items=Item.objects.all()
    popular=Popular.objects.all()
    context={
        'items':items,
        'popular':popular,
    }
    
    return render(request,'index.html',context)