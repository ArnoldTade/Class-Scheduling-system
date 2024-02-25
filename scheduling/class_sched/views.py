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


from datetime import datetime, timedelta
from .genetic_algorithm import generate_population, evolve

from django.utils import timezone
from datetime import datetime
import pytz

# Create your views here.


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
                messages.warning(request, "Invalid username or password!")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# logout page
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


# Home page
def home(request):
    instructors = Instructor.objects.all()
    return render(
        request,
        "home.html",
        {
            "instructors": instructors,
        },
    )


def home_schedule(request, id=None):
    schedules = get_object_or_404(Instructor, id=id)
    instructorSchedule = ClassSchedule.objects.filter(instructor=schedules)
    return render(
        request,
        "home.html",
        {
            "instructorSchedule": instructorSchedule,
            "instructors": Instructor.objects.all(),
        },
    )


# Schedule Table
def instructors_schedule_page(request, id=None):
    schedules = get_object_or_404(Instructor, id=id)
    instructorSchedule = ClassSchedule.objects.filter(instructor=schedules)
    if request.method == "POST":
        scheduleform = ClassScheduleForm(request.POST)
        if scheduleform.is_valid():
            scheduleform.save()
            return redirect("schedule")
    else:
        scheduleform = ClassScheduleForm()
    return render(
        request,
        "schedule.html",
        {
            "scheduleform": scheduleform,
            "instructorSchedule": instructorSchedule,
            "instructors": Instructor.objects.all(),
            "rooms": Room.objects.all(),
            "courses": Course.objects.all(),
        },
    )


@login_required
def profile(request):
    instructor = request.user.instructor
    instructorSchedule = ClassSchedule.objects.filter(instructor=instructor)

    events = []

    for schedule in instructorSchedule:
        start_time = datetime.strptime(schedule.start_time, "%H:%M").strftime(
            "%H:%M:%S"
        )
        end_time = datetime.strptime(schedule.end_time, "%H:%M").strftime("%H:%M:%S")

        # Convert days_of_week to FullCalendar format (0 for Sunday, 1 for Monday, etc.)
        days_of_week = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7,
        }.get(schedule.days_of_week)

        if days_of_week is not None:
            event = {
                "title": f"{schedule.course.course_name} - Mr.Mrs {schedule.instructor.lastName} ({schedule.room.room_name})",
                "daysOfWeek": [days_of_week],
                "startTime": start_time,
                "endTime": end_time,
            }
            events.append(event)

    return render(
        request,
        "profile.html",
        {
            "instructorSchedule": instructorSchedule,
            "events": events,
        },
    )


@login_required
def dashboard(request):
    instructors = Instructor.objects.all()
    return render(
        request,
        "dashboard.html",
        {
            "instructors": instructors,
        },
    )


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


@login_required
def schedule(request):
    instructors = Instructor.objects.all()
    return render(
        request,
        "schedule.html",
        {
            "instructors": instructors,
        },
    )


@login_required
def room(request):
    if request.method == "POST":
        roomform = RoomForm(request.POST, prefix="room")
        if roomform.is_valid():
            roomform.save()
            messages.success(request, "Room Added!")
            return redirect("room")
    else:
        roomform = RoomForm(prefix="room")

    rooms = Room.objects.all()
    schedules = ClassSchedule.objects.all()
    return render(
        request,
        "room.html",
        {
            "roomform": roomform,
            "rooms": rooms,
            "schedules": schedules,
        },
    )


# Add Subjects
@login_required
def subject(request):
    if request.method == "POST":
        subjectform = SubjectForm(request.POST, prefix="subject")
        if subjectform.is_valid():
            subjectform.save()
            messages.success(request, "Subject Added!")
            return redirect("subject")
    else:
        subjectform = SubjectForm(prefix="subject")
    courses = Course.objects.all()
    return render(
        request,
        "subject.html",
        {
            "subjectform": subjectform,
            "courses": courses,
        },
    )


# /// DELETE VIEWS ///
# Delete Subjects
def delete_subject(request, id=None):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Subject Deleted!")
    return redirect("subject")


def delete_room(request, id=None):
    room = Room.objects.get(id=id)
    room.delete()
    messages.success(request, "Room Deleted!")
    return redirect("room")


def delete_instructor(request, id=None):
    instructor = Instructor.objects.get(id=id)
    user = instructor.user_profile
    user.delete()
    instructor.delete()
    messages.success(request, "Instructor Deleted!")
    return redirect("instructors")


# /// EDIT VIEWS ///
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
    return render(request, "subject_update.html", courses)


def update_room(request, id=None):
    rooms = {}
    room = get_object_or_404(Room, id=id)
    roomform = RoomForm(request.POST, instance=room)
    if roomform.is_valid():
        roomform.save()
        messages.success(request, "Room Updated!")
        return redirect("room")

    roomform = RoomForm(instance=room)
    rooms["roomform"] = roomform
    return render(request, "room_update.html", rooms)


def update_instructor(request, id=None):
    instructors = {}
    instructor = get_object_or_404(Instructor, id=id)
    instructorform = InstructorForm(request.POST, request.FILES, instance=instructor)
    if instructorform.is_valid():
        instructorform.save()
        messages.success(request, "Instructor Updated!")
        return redirect("instructors")

    instructorform = InstructorForm(instance=instructor)
    instructors["instructorform"] = instructorform
    return render(request, "instructor_update.html", instructors)


def profile_edit(request, id=None):
    profile = {}
    instructor = get_object_or_404(Instructor, id=id)
    instructorform = InstructorForm(request.POST, request.FILES, instance=instructor)
    if instructorform.is_valid():
        instructorform.save()
        messages.success(request, "Profile Updated!")
        return redirect("profile")

    instructorform = InstructorForm(instance=instructor)
    profile["instructorform"] = instructorform
    return render(request, "profile_update.html", profile)


# GENETIC ALGORITHM


def generate_schedules(request):

    # Create an initial population of random individuals population = generate_pop(100)
    population = generate_population(100)

    # Evolve the population 100 generations
    best_individual = evolve(population, 100)

    # Extract the class schedules from the best-performing individual
    class_schedules = best_individual.class_schedules

    # Render the templates with the class schedules
    context = {"class_schedules": class_schedules}
    instructors = Instructor.objects.all()
    return render(
        request,
        "schedule.html",
        {
            "instructors": instructors,
        },
        context,
    )
