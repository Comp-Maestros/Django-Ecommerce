from django.shortcuts import render

# Create your views here.
def BlogView(request):
    context={}
    
    return render(request,'blog.html',context)