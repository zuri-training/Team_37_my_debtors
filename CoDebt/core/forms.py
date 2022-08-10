from django import forms
from django.contrib.auth. forms import UserCreationForm
from .models import CustomUser, SchoolDetail, Debtor


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    school_name = forms.CharField(max_length=50)
    sender = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'required':'required', 'placeholder': 'Enter your First Name here'}),
            'last_name': forms.TextInput(attrs={'required':'required', 'placeholder': 'Enter your Last Name here'}),
            'email': forms.EmailInput(attrs={'required':'required', 'placeholder': 'Enter your Email Address'}),
            'password1': forms.PasswordInput(attrs={'required':'required', 'placeholder': 'Create a password', 'data-toggle':'password1'}),
            'password2': forms.PasswordInput(attrs={'required':'required', 'placeholder': 'Confirm your password'})
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }

class SchoolRegistration(forms.ModelForm):
    class Meta:
        model = SchoolDetail
        fields = ('school_name', 'copy_of_CAC','CAC_number')
        widgets = {
            'copy_of_CAC':forms.FileInput(attrs={'id':'my-file','required':'required'})
        }
        labels ={
            'copy_of_CAC': 'Copy Of CAC',
            'school_name': 'School Name',
            'CAC_number': 'CAC Number'
        }

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields =  ['first_name', 'last_name', 'student_id', 'current_class', 'age', 'gender', 'academic_session', 'posted_by', 'guardian', 'student_picture', 'outstanding_fees']
        widgets = {

        }
        labels = {
            'student_id':'Student ID',
            'current_class':'Class',
            'age':'Age',
            'gender':'Gender',
            'academic_session':'Academic Session',
            'posted_by':'School name',
            'guardian':'Guardian',
            'student_picture':'Student Image',
            'outstanding_fees':'Outstanding Debt'
        }
