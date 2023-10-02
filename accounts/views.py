from django.shortcuts import render

# Create your views here.
def RegisterView(request):
    
    context={}
    
    return render(request,'accounts/register.html')


#Login View

def LoginView(request):
    
    context={}
    return render(request,'login/login.htmml',context)