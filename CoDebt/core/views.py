from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, RegisterForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def register(request):
    if request.method == 'POST':
     form = RegisterForm()
     if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Account was created for ' + username)
            user = authenticate(username=username, password=password)
            #login(request,user)
            return redirect('core/index.html')
     else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        form = RegisterForm()
        return render (request, './signup.html', {'form': form})  

    else:
        return render(request, './signup.html')   

