from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser, Debtor
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    return render(request, 'core/register.html')

def signin(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        print(email)

        user=auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home') 

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('core/signin.html')

    else:
        return render(request, 'core/signin.html')

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    messages.success(request, "Successfully signed out")
    return redirect('core/index.html')

def posts(request):
    pass

def studentprofile(request, pk):
    user_object = Debtor.objects.get(email=pk)
    user_profile = Debtor.objects.get(user= user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }

    '''
    fullname
    phone no
    email
    DOB
    address
    city
    '''
    return render(request, 'core/studentprofile.html', context)

def notification(request):
    pass