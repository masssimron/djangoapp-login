from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
#from django.contrib.messages import messages

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            #messages.error(request,'invalid')
            return redirect('error')    

    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html') 

def error(request):
    return render(request,'error.html') 

def logout(request):
    auth.logout(request)
    return render(request,'')
