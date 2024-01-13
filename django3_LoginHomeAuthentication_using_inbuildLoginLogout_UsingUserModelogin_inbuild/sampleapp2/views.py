from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib import messages
# Create your views here.


@never_cache
def print_login(request):
    if request.user.is_authenticated:    
        return redirect(print_home)
    if request.method == 'POST':
        name = request.POST['username']
        passw = request.POST['password']
        userplot = authenticate(request, username=name, password=passw)
        if userplot is not None: # step1 we create session in here
            login(request,userplot)
            return redirect(print_home)
        else:
            print("invalid username")
    return render(request, 'login.html')

@never_cache
def print_home(request):
    if request.user.is_authenticated:    
        return render(request ,'home.html')
    return redirect(print_login)



def print_logout(request):
    if request.user.is_authenticated:    
        logout(request)
    return redirect(print_login)