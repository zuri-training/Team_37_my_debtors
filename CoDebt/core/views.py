import email
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import GuardianForm, UserCreationForm, RegisterForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def register(request):
    if request.method == 'POST':
     form = RegisterForm()
     if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Account was created for ' + email)
            user = authenticate(email=email, password=password)
            login(request,user)
            return redirect(request,'core/index.html')
     else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        form = RegisterForm()
        return render (request, './signup.html', {'form': form})  

    else:
        return render(request, './signup.html')


def guardian(request):
    if request.method == 'POST':
     form = GuardianForm()
     if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Account was created for ' + username)
            user = authenticate(email=email, password=password)
            login(request,user)
            return redirect(request,'core/index.html')
     else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        form = GuardianForm()
        return render (request, './guardian.html', {'form': form})  

    else:
        return render(request, './guardian.html')           

