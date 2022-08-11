from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, SchoolDetail, Debtor
from .forms import RegistrationForm, SchoolRegistration, DebtorForm, UserComment

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register_admin(request):
    form = RegistrationForm()
    ctx = {'form':form}
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
        messages.error(request, "Please retry")
    return render(request, 'core/register-guardian.html', ctx)

def register_school(request):
    form = RegistrationForm()
    school_form = SchoolRegistration()
    if request.method=="POST":
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
            messages.error(request, "An error occurred during registration, Please try again")
    ctx = {
        'form':form, 'school_form':school_form
    }
    return render(request, 'core/register-school.html',ctx)

def login_user(request):
    if request.user.is_authenticated():
        return redirect('core:home')

    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']

        user=authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:dashboard') 

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('core:home')

    else:
        return render(request, 'core/signin.html')

#the login required ensures the user is signed in before he can signout and directs him to the signin
'''@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, "Successfully signed out")
    return redirect('core/index.html')'''

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

def studentprofile(request, student_id):
    student = Debtor.objects.get(student_id=student_id)

    ctx = {
        'school': SchoolDetail.objects.get(school=student.posted_by.id),
        'student': student,
    }
    return render(request, 'core/studentprofile.html', ctx)
'''def studentprofile(request, pk):
    user_object = Debtor.objects.get(email=pk)
    user_profile = Debtor.objects.get(user= user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'core/studentprofile.html', context)'''

def addDebtor(request):
    form = DebtorForm()
    if request.method=='post':
        form = DebtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:admin_dashboard')
        messages.error(request, 'Unable to add debtor. Please try again.')
    
    ctx = {'form': form}
    return render(request, 'core/adddebtor.html', ctx)

def updateDebtor(request, student_id):
    debtor = Debtor.objects.get(student_id=student_id)
    form = DebtorForm(instance=debtor)

    if request.method=='post':
        form = DebtorForm(request.POST, instance=debtor)
        if form.is_valid():
            form.save()
            return redirect('core:admin_dashboard')
        messages.error(request, 'Unable to update debtor. Please try again.')
    
    ctx = {'form': form}
    return render(request, 'core/adddebtor.html', ctx)
    
def deleteDebtor(request, student_id):
    debtor = Debtor.objects.get(student_id=student_id)
    debtor.delete()
    return redirect('core:admin_dashboard')


def search(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    debtors = Debtor.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(student_id__icontains=q)
    )

    ctx = {'debtors': debtors}
    return render(request, ctx)

def make_comment(request):
    comment_form = UserComment(request.POST or None)
    user_commenting = request.user
    post_commenting_on = get_object_or_404(Debtor)
    if request.method == 'POST':
        print(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user_commenting = user_commenting
            new_comment.posted_on = post_commenting_on
            new_comment.save()
    context = {
        'comment_form': comment_form,
        'commenter': user_commenting,
        'commenting_on': post_commenting_on
    }
    return render(request, 'core/comment.html', context)