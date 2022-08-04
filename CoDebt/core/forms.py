from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import CustomUser

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
    