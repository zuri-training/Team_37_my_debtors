from django import forms
from django.contrib.auth. forms import UserCreationForm
from .models import CustomUser, SchoolDetail, Debtor


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
        fields = ('school_name','CAC_number')
        widgets = {
            # 'copy_of_CAC':forms.FileInput(attrs={'id':'my-file','required':'required'})
        }
        labels ={
            # 'copy_of_CAC': 'Copy Of CAC',
            'school_name': 'School Name',
            'CAC_number': 'CAC Number'
        }

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields =  ['first_name', 'last_name', 'student_id', 'current_class', 'age', 'gender', 'academic_session', 'address', 'debt_type', 'student_picture', 'outstanding_fees']
        widgets = {
            'first_name': forms.TextInput(attrs={'required':'required', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'required':'required', 'placeholder': 'Last Name'}),
            'student_id': forms.TextInput(attrs={'required':'required', 'placeholder': 'Student ID'}),
            'current_class': forms.TextInput(attrs={'required':'required', 'placeholder': 'Class'}),
            'age': forms.NumberInput(attrs={'required':'required', 'placeholder': 'Age'}),
            'gender': forms.TextInput(attrs={'required':'required', 'placeholder': 'M/F'}),
            'academic_session': forms.TextInput(attrs={'required':'required', 'placeholder': 'Academic Session'}),
            'address': forms.TextInput(attrs={'required':'required', 'placeholder': 'Address'}),
            'debt_type': forms.TextInput(attrs={'required':'required', 'placeholder': 'Nature of debt(School Fees, Books etc.)'}),
            'student_picture': forms.FileInput(attrs={'required':'required',}),
            'outstanding_fees': forms.NumberInput(attrs={'required':'required', 'placeholder': 'Amount Owed'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'student_id':'Student ID',
            'current_class':'Class',
            'age':'Age',
            'gender':'Gender',
            'academic_session':'Academic Session',
            'debt_type':'Payment For',
            'address':'Address',
            'student_picture':'Student Image',
            'outstanding_fees':'Outstanding Debt'
        }