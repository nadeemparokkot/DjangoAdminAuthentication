from django.shortcuts import render,redirect
from . models import LoginInfo
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
# Create your views here.

@never_cache
def print_login(request):
    if 'hai' in request.session: 
        return redirect(print_home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LoginInfo.objects.get(name=username)  # Retrieve user object
        if user is not None:            
            request.session['hai']=username
            return redirect(print_home)
            
        else:
            print('User not found')
        # userplot = authenticate(request, username=name, password=passw)
        # if userplot is not None:
        #     login( request,userplot)
        #     return redirect(print_home)
        # else:
        #     print("invalid username")
    return render(request, 'login.html')
    
def print_signup(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        login_obj=LoginInfo(name=username,password=password)
        login_obj.save()
    return render(request,'signup.html')

@never_cache
def print_home(request):
    if 'hai' in request.session: # step2 if we use this cannot get access to move home page without valid user name
        return render(request,'homepage.html')
    return redirect(print_login)

def print_save(request):
    saveddata=LoginInfo.objects.all()
    return render(request,'saveddata.html',{'data':saveddata})

def print_logout(request):
    if 'hai' in request.session:
        del request.session["hai"]    
        # request.session.flush()
    return redirect(print_login)