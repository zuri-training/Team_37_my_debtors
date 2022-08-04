from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'name',
            'school_name',
            'avatar',
            'password1',
            'password2',
        )

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.name = self.cleaned_data['name']
    #     user.email = self.cleaned_data['email']

    #     if commit:
    #         user.save()
    #     return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'name',
            'school_name',
            'avatar',
            )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Enter First Name')
    last_name = forms.CharField(max_length=50, required=True, help_text='Enter Last Name')
    school_name = forms.CharField(max_length= 50, required=True)
    email = forms.EmailField(max_length=50, help_text='Required. Input a valid email address.')
    username = forms.CharField(max_length=200,required = True, help_text='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(help_text='Enter Password Again',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)

    
    class Meta:
        model = User
        fields = ('username', 
        'first_name', 
        'last_name',
        'school_name', 
        'email', 
        'password1',
         'password2', )    
