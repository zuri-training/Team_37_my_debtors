import numbers
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, SchoolDetail
from .forms import RegistrationForm, SchoolRegistration

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register_admin(request):
    form = RegistrationForm()
    ctx ={'form': form}
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        else:
            messages.error(request, 'Please retry')
    return render(request, 'core/register-guardian.html', ctx)

def register_school(request):
    form = RegistrationForm()
    school_form = SchoolRegistration()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        school_form = SchoolRegistration(request.POST, request.FILES)
        if form.is_valid() and school_form.is_valid():
            user = form.save(commit=False)
            user.save()
            SchoolDetail.objects.create(
                school=user,
                school_name=request.POST.get('school_name'),
                copy_of_CAC=request.FILES['copy_of_CAC'],
                CAC_number=request.POST['CAC_number'],
            )
            return redirect('core:home')
        else:
            messages.error(request, 'An error occurred during registration, Please try again')
    ctx = {'form':form, 'school_form':school_form}
    return render(request, 'core/register-school.html',ctx)

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
        messages.info(request, 'You are already signed out')
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

def dashboard(request):
    pass