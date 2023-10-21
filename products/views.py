from django.shortcuts import render

# Create your views here.
def ProductView(request):
    
    context={}
    
    return render(request,'product.html')