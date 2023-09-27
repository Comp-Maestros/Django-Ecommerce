from django.shortcuts import render

# Create your views here.
def ContactView(request):
    
    context={}
    return render(request,'contact/contact.html')