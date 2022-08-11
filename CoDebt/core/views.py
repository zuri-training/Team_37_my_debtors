from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SchoolDetail, Debtor
from .forms import RegistrationForm, SchoolRegistration
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def email_sender(user):
    subject = 'We are glad to have you at CoDebt'
    recipient_list = [user.email,]
    email_from = settings.EMAIL_HOST_USER
    content = f'Hi {user}. Thank you for signing up on CoDebet. We promise to help you recover your debts easily and promptly. Cheers'

    send_mail(subject, content, email_from, recipient_list)

def register_users(request):
    form = RegistrationForm()
    ctx ={'form': form}
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email_sender(user)
            user.save()
            return redirect('core:home')
        else:
            messages.error(request, 'An error occured, Please retry')
    return render(request, 'core/register-guardian.html', ctx)

def register_school(request):
    form = RegistrationForm()
    school_form = SchoolRegistration()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        school_form = SchoolRegistration(request.POST, request.FILES)
        if form.is_valid() and school_form.is_valid():
            user = form.save(commit=False)
            email_sender(user)
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
            return redirect('core:dashboard')
        
        messages.error(request, 'Invalid credentials')
        return redirect('core:login')    
    return render(request, 'core/login.html')


def logout_user(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not signed in')
        return redirect('core:home')

    logout(request)
    return redirect('core:home')

def contact_us(request):
    if request.method == 'POST':
        pass

    return render(request, 'core/contact.html')

def testimonials(request):
    pass

def about_us(request):
    return render(request, 'core/about-us.html')

@login_required()
def dashboard(request):
    user = request.user
    all_time_debt = Debtor.all_objects.all().count()
    all_time_debt = all_time_debt if all_time_debt > 0 else 1
    recovered_debts = Debtor.all_objects.filter(posted_by=user, is_deleted=True).count()
    debt_count = Debtor.objects.filter(posted_by=user).count()

    recovered_percent = (recovered_debts * 100) / all_time_debt
    indebted_percent = (debt_count * 100) / all_time_debt
    
    ctx = {
        'user':user,
        'count': debt_count,
        'indebted_percent': indebted_percent,
        'recovered': recovered_debts,
        'recovered_percent': recovered_percent,
        }
    return render(request, 'core/admin-dashboard.html',ctx)

def studentprofile(request, pk):
    student = Debtor.objects.get(id=pk)

    ctx = {
        'school': SchoolDetail.objects.get(school=student.posted_by.id),
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

    ctx = {'debtors': debtors}
    return render(request, ctx)