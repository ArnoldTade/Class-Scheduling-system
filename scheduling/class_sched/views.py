from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm


# Create your views here.


# For User Registration


# signup page
def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


# login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
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
