from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.


# For User Registration


# signup page
@login_required
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
                messages.success(request, "Successfully Registered!")
            return redirect("instructors")
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


# Add Subjects


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
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


# END User Registration


def home(request):
    return render(request, "home.html")


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def instructors(request):
    return render(request, "instructors.html")


@login_required
def schedule(request):
    return render(request, "schedule.html")


@login_required
def subject(request):
    if request.method == "POST":
        subjectform = SubjectForm(request.POST)
        if subjectform.is_valid():
            subjectform.save()
            messages.success(request, "Subject Added!")
            return redirect("subject")
    else:
        subjectform = SubjectForm()

    courses = Course.objects.all()
    return render(
        request,
        "subject.html",
        {
            "subjectform": subjectform,
            "courses": courses,
        },
    )


def delete_subject(request, id=None):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Deleted!")
    return redirect("subject")
