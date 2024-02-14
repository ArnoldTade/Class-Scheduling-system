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
            "profile_picture",
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
            "role",
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "course_name",
            "description",
            "credits",
            "prerequisites",
        ]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_name",
            "department",
        ]
