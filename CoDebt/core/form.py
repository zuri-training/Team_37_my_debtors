from tkinter import Widget
from django import forms
from .models import Debtors


#  Create your form here
class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ('posted_by', 'first_name', 'last_name', 'school_name', 'student_id', 'outstanding_fees', 'is_contending_debt')
        widgets = {
            'posted_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lastname', 'required': 'required'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School name', 'required': 'required'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID', 'required': 'required'}),
            'outstanding_fees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount oweing', 'required': 'required'}),
            'is_contending_debt':forms.NullBooleanSelect(attrs={'class': 'form-control'})
        }

# In-line html JavaScript for the widget - "posted_by", to automatically generate the author of the post from loggedin credentials
'''
    <!-- Automatically generate the autors name based on logged in -->
    <script>
        var name = "{{ user.first_name }} {{ user.last_name }}";
        document.getElementById("author").value = name;
    </script>
'''