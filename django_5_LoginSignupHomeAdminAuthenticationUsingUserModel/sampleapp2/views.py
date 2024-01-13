from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
# Create your views here.

@never_cache
def print_login(request):
    if request.user.is_authenticated:    
        return redirect(print_home)
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(print_home)
        else:
            if User.objects.filter(username=username):
                messages.add_message(request, messages.WARNING, 'Invalid password')
            else:
                messages.add_message(request, messages.WARNING, 'User not found')
    return render(request, 'login.html')

@never_cache
def print_signup(request):
    if request.user.is_authenticated:    
        return redirect(print_home)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username):
                messages.add_message(request,messages.WARNING, "!!! Username Already Exist !!!")
            elif User.objects.filter(email=email):
                messages.add_message(request,messages.WARNING, "!!! Email Already exist !!!")
            else:
                password = make_password(password, salt=None, hasher="pbkdf2_sha256")
                user = User(username=username, email=email, password=password)
                user.save()
                user = authenticate(request ,username=username, password=password2)
                login(request, user)
                return redirect(print_home)          
        else:
            messages.add_message(request,messages.WARNING,"!!! Password not matching !!!")
    return render(request, 'signup.html')

@never_cache
def print_home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/useradmin')
        return render(request, 'home.html')
    return redirect(print_login)
    
def print_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(print_login)