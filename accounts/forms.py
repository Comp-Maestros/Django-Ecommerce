
# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
