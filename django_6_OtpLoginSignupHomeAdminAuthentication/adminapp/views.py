from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from django.contrib import messages


# Create your views here.
@never_cache
def user_admin(request):
    
    if request.user.is_superuser:
        if request.method == 'POST':
            search_word = request.POST['search-word']
            data = User.objects.filter(Q(username__icontains=search_word)| Q(email__icontains=search_word)).order_by('id').values()
        else:
            data = User.objects.all().order_by('id').values()
        context = {'members': data}
        return render(request, 'useradmin.html', context)
    return redirect(user_admin)

def user_delete(request, pk):
    if request.user.is_superuser:
        if User.objects.filter(id=pk):
            user = User.objects.get(id=pk)
            print(user)
            if not user.is_superuser: 
                user.delete()
    return redirect(user_admin)

@never_cache
def user_edit(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
            if User.objects.filter(id=pk):
                user = User.objects.get(id=pk)
                context = {
                    'user' : user
                }
                return render(request, 'useredit.html', context=context)
        elif request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password = make_password(password, salt=None, hasher="pbkdf2_sha256")
            if User.objects.filter(id=pk):
                user = User.objects.get(id=pk)
                if email and user.email != email:
                    print(user.email)
                    print(email)
                    if User.objects.filter(email=email):
                        messages.add_message(request, messages.WARNING, 'email exist')
                        return render(request, 'useredit.html')
                    else:
                        user.email = email
                if username and user.username != username :
                    if User.objects.filter(username=username):
                        messages.add_message(request, messages.WARNING, 'username exist')
                        return render(request, 'useredit.html')
                    else:
                        user.username = username
                if password is not None : 
                    user.password = password
                    user.save()                
        return redirect(user_admin)

@never_cache
def user_add(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password = make_password(password, salt=None, hasher="pbkdf2_sha256")
            if User.objects.filter(username=username):
                messages.add_message(request, messages.WARNING, 'username exist')
                return render(request, 'useradd.html')
            elif User.objects.filter(email=email):
                messages.add_message(request, messages.WARNING, 'email exist')
                return render(request, 'useradd.html')
            else:
                user = User(username=username, email=email, password=password)
                user.save()
            return redirect(user_admin)
        return render(request, 'useradd.html')
    
        