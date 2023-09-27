from django.shortcuts import render

# Create your views here.
def AboutView(request):
    
    context={}
    
    return render(request,'about.html',context)