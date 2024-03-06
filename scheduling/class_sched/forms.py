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
            "middleName",
            "gender",
            "email",
            "contact",
            "birthday",
            "address",
            "college",
            "status",
            "role",
            "course_handled",
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
            "type",
            "college",
            "course",
            "semester",
            "year_level",
        ]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_name",
            "college",
            "room_type",
        ]


class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = [
            "course",
            "instructor",
            "room",
            "start_time",
            "end_time",
            "days_of_week",
            "semester",
            "year",
        ]


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = [
            "day",
        ]


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            "program_section",
            "section_college",
            "number_students",
        ]


class InstructorCourseForm(forms.ModelForm):
    class Meta:
        model = InstructorCourse
        fields = [
            "instructor",
            "course",
            "sections",
        ]
