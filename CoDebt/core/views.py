from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SchoolDetail, Debtor
from .forms import RegistrationForm, SchoolRegistration, ContactForm, DebtorForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def email_sender(user):
    subject = 'We are glad to have you at CoDebt'
    recipient_list = [user.email,]
    email_from = settings.EMAIL_HOST_USER
    content = f'Hi {user}. Thank you for signing up on CoDebt. We promise to help you recover your debts easily and promptly. Cheers'

    send_mail(subject, content, email_from, recipient_list)

def register_users(request):
    form = RegistrationForm()
    ctx ={'form': form}
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_guardian = True
            email_sender(user)
            user.save()
            return redirect('core:home')
        else:
            messages.info(request, 'An error occured, Please retry. Enter a strong password')
    return render(request, 'core/register-guardian.html', ctx)

def register_school(request):
    form = RegistrationForm()
    school_form = SchoolRegistration()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        school_form = SchoolRegistration(request.POST)
        if form.is_valid() and school_form.is_valid():
            user = form.save(commit=False)
            user.is_school_admin = True
            email_sender(user)
            user.save()
            SchoolDetail.objects.create(
                school=user,
                school_name=request.POST.get('school_name'),
                CAC_number=request.POST['CAC_number'],
            )
            return redirect('core:login')
        else:
            messages.error(request, 'An error occurred during registration, Please try again. Enter a strong password')
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
            if user.is_school_admin:
                return redirect('core:dashboard')
            return redirect('core:home')
        
        messages.info(request, 'Invalid credentials')
        return redirect('core:login')    
    return render(request, 'core/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not signed in')
        return redirect('core:home')

    logout(request)
    messages.success(request, 'You have successfully signed out')
    return redirect('core:login')

def contact_us(request):
    return render(request, 'core/contact.html')

def about_us(request):
    return render(request, 'core/about-us.html')

@login_required()
def dashboard(request):
    user = request.user
    if not request.user.is_school_admin:
        messages.info(request, 'Only school admins can access here!')
        return redirect('core:home')
    all_time_debt = Debtor.all_objects.all().count()
    all_time_debt = all_time_debt if all_time_debt > 0 else 1
    school = SchoolDetail.objects.get(school=user.id)
    recovered_debts = Debtor.all_objects.filter(posted_by=school, is_deleted=True).count()
    debt_count = Debtor.objects.filter(posted_by=school).count()

    recovered_percent = (recovered_debts * 100) / all_time_debt
    indebted_percent = (debt_count * 100) / all_time_debt
    form = DebtorForm()
    ctx = {
        'user':user,
        'count': debt_count,
        'indebted_percent': indebted_percent,
        'recovered': recovered_debts,
        'recovered_percent': recovered_percent,
        'form': form,
        }
    return render(request, 'core/admin-dashboard.html',ctx)

def studentprofile(request, pk):
    student = Debtor.objects.get(id=pk)

    ctx = {
        'school': student.posted_by,
        'student': student,
    }
    return render(request, 'core/studentprofile.html', ctx)

def schoolprofiles(request, pk):
    school = SchoolDetail.objects.get(id=pk)
    school_admin = school.school
    ctx = {
        'school':school,
        'school_admin': school_admin
    }
    return render(request, 'core/adminprofile.html', ctx)

def search(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    debtors = Debtor.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(student_id__icontains=q)
    )
    school = SchoolDetail.objects.get(school=request.user)

    ctx = {'debtors': debtors, 'school':school}
    return render(request,'core/debtor-list.html', ctx)

def add_debtor(request):
    if request.method == 'POST':
     form = DebtorForm(request.POST)
     if form.is_valid():
        debtor = form.save(commit=False)
        debtor.posted_by = SchoolDetail.objects.get(school=request.user)
        debtor.save()
        messages.success(request, 'Debtor add successful')
    else:
        messages.info(request, 'Invalid Input')
    return redirect('core:dashboard')

def resolve(request, pk):
    debtor = Debtor.objects.get(id=pk)
    debtor.soft_delete()
    return redirect('core:search')