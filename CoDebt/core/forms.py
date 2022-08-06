from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Comment
from django import forms
from tkinter import Widget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'school_name',
            'avatar',
            'password1',
            'password2',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'school_name',
            'avatar',
        )


class UserComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
        )

        widgets = {
            # 'user_commenting': forms.TextInput(attrs= {'class': 'form-control', 'id': 'author', 'value': '',
            # 'type': 'hidden'}), 'posted_on': forms.TextInput(attrs= {'class': 'form-control', 'id': 'debtor-post',
            # 'value': '', 'type': 'hidden'}),
            'comment': forms.TextInput(attrs=
                                       {'class': 'form-control', 'placeholder': 'Comment', 'required': 'required'})
        }
