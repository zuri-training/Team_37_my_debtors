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
    