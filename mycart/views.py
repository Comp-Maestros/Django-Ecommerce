from django.shortcuts import render

# Create your views here.
    
def CartView(request):
    return render(request, 'cart/cart.html')

def Shopping(request):
    
    return render(request,'cart/shop.html')