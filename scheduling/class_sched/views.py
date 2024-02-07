from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.


# For User Registration


# signup page
def user_signup(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        instructor_form = InstructorForm(request.POST)

        if userform.is_valid() and instructor_form.is_valid():
            with transaction.atomic():
                user = userform.save()
                instructor = instructor_form.save(commit=False)
                instructor.user_profile = user
                instructor.save()
            return redirect("login")
    else:
        userform = UserCreationForm()
        instructor_form = InstructorForm()

    return render(
        request,
        "signup.html",
        {
            "userform": userform,
            "instructor_form": instructor_form,
        },
    )


# login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    instructor = Instructor.objects.get(user_profile=user)
                    if instructor.role == "Admin":
                        return redirect("dashboard")
                    elif instructor.role == "User":
                        return redirect("profile")
                except Instructor.DoesNotExist:
                    pass
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# logout page
def user_logout(request):
    logout(request)
    return redirect("login")


# END User Registration


def home(request):
    return render(request, "home.html")


@login_required
def profile(request):
    return render(request, "profile.html")


def dashboard(request):
    return render(request, "dashboard.html")


def instructors(request):
    return render(request, "instructors.html")


def schedule(request):
    return render(request, "schedule.html")


def about(request):
    return render(request, "about.html")
