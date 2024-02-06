from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            "firstName",
            "lastName",
            "suffix",
            "gender",
            "email",
            "contact",
            "birthday",
            "address",
            "department",
            "time_availability",
            "profile_pic",
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
