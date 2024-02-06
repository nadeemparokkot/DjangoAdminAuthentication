from audioop import reverse
from datetime import timedelta,datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
import random
from django.core.mail import send_mail
from django.http import JsonResponse

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
        request.session['user_email'] = email
        
        if password == password2:
            if User.objects.filter(username=username):
                messages.add_message(request,messages.WARNING, "!!! Username Already Exist !!!")
            elif User.objects.filter(email=email).first():
                messages.add_message(request,messages.WARNING, "!!! Email Already exist !!!")
                return redirect(print_signup)
            else:
                password = make_password(password, salt=None, hasher="pbkdf2_sha256")
                user = User(username=username, email=email, password=password)
                user.save()
                user = authenticate(request ,username=username, password=password2)
                login(request, user)
                #request.session['registration_form_data'] = form.cleaned_data
                otp = random.randint(100000, 999999)
                request.session['otp'] = str(otp)
                expiration_time = timezone.now() + timedelta(minutes=1)
                request.session['otp_expiry_time'] = expiration_time.isoformat()
                send_mail(
                    'OTP Verification',
                    'Merin nte otp he he he ' + str(otp),
                    'nadeemparokkot@gmail.com',
                    [email],
                    fail_silently=False,
                 )
                return redirect(print_otp)
                
                  
        else:
            messages.add_message(request,messages.WARNING,"!!! Password not matching !!!")
    return render(request, 'signup.html')
@never_cache
def print_otp(request):
    if 'otp' in request.session: 
        if request.method == 'POST':
            otp = request.POST.get('otp')
            otp_expiry_time_str = request.session.get('otp_expiry_time')
            otp_expiry_time = datetime.fromisoformat(otp_expiry_time_str)


            if otp == request.session.get('otp') and timezone.now() <= otp_expiry_time:
                # request.session.flush()
                return redirect(print_home)
            else:
                messages.error(request, 'Invalid or expired OTP')
                

        return render(request,'verifyotp.html')

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

def print_timeout(request):
    

    return render(request, 'timeout.html')

def print_resend_otp(request):
    # Generate a new OTP and send it to the user
    otp = random.randint(100000, 999999)
    request.session['otp'] = str(otp)
    expiration_time = timezone.now() + timedelta(minutes=1)
    request.session['otp_expiry_time'] = expiration_time.isoformat()  # Expires after 1 minute
    email = request.session.get('user_email')
    # Replace 'email' with the actual email address of the user
    send_mail(
        'OTP Verification',
        'Merin nte otp he he he ' + str(otp),
        'nadeemparokkot@gmail.com',
        [email],  # Replace with the actual email address
        fail_silently=False,
    )

    # Redirect to the OTP verification page
    print(otp)
    return redirect(print_otp)
