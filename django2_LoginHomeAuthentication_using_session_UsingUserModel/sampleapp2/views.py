from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache #we can use never_cashe for to disable browser back button
def print_login(request):
    if 'username' in request.session: #step3 after login user nn login page kanaan paadilla 
        return redirect(print_home)
    if request.method == 'POST':
        usern = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=usern, password=passw)
        if user is not None: # step1 we create session in here username keyword aaki using session
            request.session['username']=usern
            
            return redirect(print_home)
        else:
            print("invalid username or password")
    return render(request, 'login.html')

@never_cache
def print_home(request):
    if 'username' in request.session: # step2 if we use this cannot get access to move home page without valid user name
        return render(request ,'home.html')
    return redirect(print_login)



def print_logout(request):
    if 'username' in request.session:
        request.session.flush() #after logout they never see again home page for that we use flush
    return redirect(print_login)