from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register_admin(request):
    return render(request, 'core/register-guardian.html')

def register_school(request):
    return render(request, 'core/register-school.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.error(request, 'Invalid credentials')
        return redirect('core:login')    
    return render(request, 'core/login.html')

@login_required()
def logout_user(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('core:home')
    logout(request)
    messages.success(request, 'You have successfully signed out')
    return redirect('core:home')

def contact_us(request):
    if request.method == 'POST':
        pass

    return render(request, 'core/contact.html')

def about_us(request):
    return render(request, 'core/about-us.html')

def password_reset(request):
    pass