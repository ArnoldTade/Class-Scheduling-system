from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
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
        instructor_form = InstructorForm(request.POST, request.FILES)

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
    instructors = Instructor.objects.all()
    return render(
        request,
        "home.html",
        {
            "instructors": instructors,
        },
    )


def profile_edit(request):
    instructor = get_object_or_404(Instructor, id=id)
    instructorform = InstructorForm(request.POST, instance=instructor)
    if instructorform.is_valid():
        instructor = instructorform.save(commit=False)
        instructor.save()
        messages.success(request, "Profile Updated!")
        instructors = {"instructorform": instructorform}
        return redirect("profile")
    else:
        instructors = {
            "instructorform": instructorform,
            "error": "The Form was not updated",
        }
        return render(request, "profile.html", instructors)


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def instructors(request):
    instructors = Instructor.objects.all()
    return render(
        request,
        "instructors.html",
        {
            "instructors": instructors,
        },
    )


# Delete Instructor
def delete_instructor(request, id=None):
    instructor = Instructor.objects.get(id=id)
    instructor.delete()
    messages.success(request, "Instructor Deleted!")
    return redirect("instructors")


@login_required
def schedule(request):
    return render(request, "schedule.html")


# Add Subjects
@login_required
def subject(request):
    if request.method == "POST":
        subjectform = SubjectForm(request.POST, prefix="subject")
        roomform = RoomForm(request.POST, prefix="room")
        if "add_subject" in request.POST and subjectform.is_valid():
            subjectform.save()
            messages.success(request, "Subject Added!")
            return redirect("subject")
        elif "add_room" in request.POST and roomform.is_valid():
            roomform.save()
            messages.success(request, "Room Added!")
            return redirect("subject")
    else:
        subjectform = SubjectForm(prefix="subject")
        roomform = RoomForm(prefix="room")

    courses = Course.objects.all()
    rooms = Room.objects.all()
    return render(
        request,
        "subject.html",
        {
            "subjectform": subjectform,
            "roomform": roomform,
            "courses": courses,
            "rooms": rooms,
        },
    )


# Delete Subjects
def delete_subject(request, id=None):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Subject Deleted!")
    return redirect("subject")


# Delete Rooms
def delete_room(request, id=None):
    room = Room.objects.get(id=id)
    room.delete()
    messages.success(request, "Room Deleted!")
    return redirect("subject")


# Edit Subjects
def update_subject(request, id=None):
    courses = {}
    course = get_object_or_404(Course, id=id)
    courseform = SubjectForm(request.POST, instance=course)
    if courseform.is_valid():
        courseform.save()
        messages.success(request, "Subject Updated!")
        return redirect("subject")

    courseform = SubjectForm(instance=course)
    courses["courseform"] = courseform
    return render(request, "subject.html", courses)


# Edit Instructors
def update_instructor(request, id=None):
    instructors = {}
    instructor = get_object_or_404(Instructor, id=id)
    instructorform = InstructorForm(request.POST, instance=instructor)
    if instructorform.is_valid():
        instructorform.save()
        messages.success(request, "Instructor Updated!")
        return redirect("instructors")

    instructorform = InstructorForm(instance=instructor)
    instructors["instructorform"] = instructorform
    return render(request, "instructors.html", instructors)
