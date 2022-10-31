from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import UpdateUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required

# Create your views here.

@never_cache
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, 'signup.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                if request.user.is_superuser:
                    return redirect('admin_panel')
                else:
                    return redirect('/')
        else:
            messages.info(request, "Password doesn't match")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

@never_cache
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            if request.user.is_superuser:
                return redirect('admin_panel')
            else:
                return redirect('/')
        else:
            messages.info(request, 'Enter valid Username or Password')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

@never_cache
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('/login')

@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        return redirect("/login")

@login_required(login_url='login')
@never_cache
def products(request):
    return render(request, 'products.html')
    
@login_required(login_url='login')
@never_cache
def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html')

@login_required(login_url='login')
@never_cache
def admin_panel(request):
    if request.user.is_authenticated:
        Users = User.objects.filter(is_superuser = False)
        context = {
            "UserList": Users,
            'currentsite':get_current_site(request)
        }
        return render(request,"admin.html",context)
    else:
        return redirect("/login")

@never_cache
@login_required(login_url='login')
def edit(request, id):
    Users = User.objects.filter(id=id)  
    context = {
        "Users":Users
    }
    return render(request, 'edit.html',context)

@never_cache
@login_required(login_url='login')
def update(request, id):
    if request.user.is_authenticated:
        Users = User.objects.get(id=id)
        form = UpdateUserForm(request.POST, instance=Users)
        if form.is_valid():
            form.save()
            return redirect("admin_panel")
        else:
            messages.info(request, 'Username or email already taken')
            return redirect('edit',id=id) 
    else:
        return redirect("login")

@login_required(login_url='login')
def delete(request, id):
    Users = User.objects.filter(id=id)  
    Users.delete()
    return redirect('admin_panel')
