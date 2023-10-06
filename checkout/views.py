from django.shortcuts import render

# Create your views here.
def CheckoutView(request):
    
    return render(request,'checkout/checkout.html')