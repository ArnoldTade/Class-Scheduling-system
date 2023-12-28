from django.shortcuts import render, redirect

# Create your views here.


def dashboard(request):
    return render(request, "dashboard.html")


def instructors(request):
    return render(request, "instructors.html")


def schedule(request):
    return render(request, "schedule.html")


def about(request):
    return render(request, "about.html")
