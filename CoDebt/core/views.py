from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    # form = CustomUserCreationForm()
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         messages.info(request, 'Thanks for registering. You are now logged in')
    #         user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
    #         login(request, user)
    #         return redirect('core:home')

    # ctx = {'form':form}
    print(request)
    return render(request, 'core/register.html')

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

def logout_user(request):
    if not request.user.is_authenticated:
       return redirect('core:home')
    logout(request)
    messages.success(request, 'Successfully signed out')
    return redirect('core:home')

def contact_us(request):
    return render(request, 'core/contact.html')