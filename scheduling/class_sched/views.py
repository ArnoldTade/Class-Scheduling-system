from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import transaction

from datetime import datetime, timedelta
from .genetic_algorithm import generate_population, evolve
from .sampleTest import viewData
from django.utils import timezone
from datetime import datetime, time
import pytz

from collections import defaultdict
from .class_scheduling import *
from django.db.models import Sum
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.


### signup page ###
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
                selected_courses = request.POST.getlist("course_handled")
                instructor.course_handled.set(selected_courses)
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
            "courses": Course.objects.all(),
            "sections": Section.objects.all(),
        },
    )


### login page ###
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


#### logout page ###
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


### Home page ###
def home(request):
    instructors = Instructor.objects.all()
    return render(
        request,
        "home.html",
        {
            "instructors": instructors,
        },
    )


def conflict(request):
    return render(
        request,
        "conflict.html",
    )


@login_required
def summary(request):
    class_schedules = ClassSchedule.objects.all().order_by("instructor__lastName")
    return render(
        request,
        "summary.html",
        {
            "class_schedules": class_schedules,
        },
    )


@login_required
def generate_schedule(request):
    instructors = Instructor.objects.all()
    sections = Section.objects.all()
    instructor_course = InstructorCourse.objects.all()
    return render(
        request,
        "generate_schedule.html",
        {
            "instructors": instructors,
            "sections": sections,
            "instructor_course": instructor_course,
        },
    )


@login_required
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


### Schedule Table ###
@login_required
def instructors_schedule_page(request, id=None):
    schedules = get_object_or_404(Instructor, id=id)
    instructorSchedule = ClassSchedule.objects.filter(instructor=schedules)
    eventSchedules = []
    if request.method == "POST":
        scheduleform = ClassScheduleForm(request.POST)
        if scheduleform.is_valid():
            scheduleform.save()
            return redirect("schedule")
    else:
        scheduleform = ClassScheduleForm()

    for schedule in instructorSchedule:
        start_time = datetime.strptime(schedule.start_time, "%H:%M").strftime(
            "%H:%M:%S"
        )
        end_time = datetime.strptime(schedule.end_time, "%H:%M").strftime("%H:%M:%S")

        days_of_week_mapping = {
            "M": 1,
            "T": 2,
            "W": 3,
            "H": 4,
            "F": 5,
            "S": 6,
            "Sunday": 7,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
        }  # .get(schedule.days_of_week)
        days_of_week = list(schedule.days_of_week)

        if days_of_week is not None:
            eventSchedule = {
                "title": f"{schedule.course.course_name} - Mr/Mrs. {schedule.instructor.lastName} ({schedule.room.room_name}) - {schedule.section}",
                "daysOfWeek": [
                    days_of_week_mapping[day]
                    for day in days_of_week
                    if day in days_of_week_mapping
                ],
                "startTime": start_time,
                "endTime": end_time,
            }
            eventSchedules.append(eventSchedule)
    class_schedules = ClassSchedule.objects.all()
    total_conflicts = sum(schedule.has_conflict() for schedule in class_schedules)
    total_hours = instructorSchedule.aggregate(total_hours=Sum("course__hours"))[
        "total_hours"
    ]
    total_units = instructorSchedule.aggregate(total_hours=Sum("course__credits"))[
        "total_hours"
    ]
    total_units = int(total_units) if total_units is not None else 0
    return render(
        request,
        "schedule.html",
        {
            "scheduleform": scheduleform,
            "instructorSchedule": instructorSchedule,
            "instructors": Instructor.objects.all(),
            "rooms": Room.objects.all(),
            "courses": Course.objects.all(),
            "sections": Section.objects.all(),
            "eventSchedules": eventSchedules,
            "total_conflicts": total_conflicts,
            "schedules": schedules,
            "total_hours": total_hours,
            "total_units": total_units,
        },
    )


@login_required
def profile(request):
    instructor = request.user.instructor
    instructorSchedule = ClassSchedule.objects.filter(instructor=instructor)
    instructor_data = instructor
    total_hours = instructorSchedule.aggregate(total_hours=Sum("course__hours"))[
        "total_hours"
    ]
    total_units = instructorSchedule.aggregate(total_hours=Sum("course__credits"))[
        "total_hours"
    ]
    total_units = int(total_units) if total_units is not None else 0
    events = []

    for schedule in instructorSchedule:
        start_time = datetime.strptime(schedule.start_time, "%H:%M").strftime(
            "%H:%M:%S"
        )
        end_time = datetime.strptime(schedule.end_time, "%H:%M").strftime("%H:%M:%S")

        # Convert days_of_week to FullCalendar format (0 for Sunday, 1 for Monday, etc.)
        days_of_week_mapping = {
            "M": 1,
            "T": 2,
            "W": 3,
            "H": 4,
            "F": 5,
            "S": 6,
            "Sunday": 7,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
        }  # .get(schedule.days_of_week)
        days_of_week = list(schedule.days_of_week)
        if days_of_week is not None:
            event = {
                "title": f"{schedule.course.course_name} - Mr/Mrs. {schedule.instructor.lastName} ({schedule.room.room_name})",
                "daysOfWeek": [
                    days_of_week_mapping[day]
                    for day in days_of_week
                    if day in days_of_week_mapping
                ],
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
            "instructor_data": instructor_data,
            "instructors": Instructor.objects.all(),
            "total_hours": total_hours,
            "total_units": total_units,
        },
    )


@login_required
def dashboard(request):
    all_instructors = Instructor.objects.all()
    instructors = Instructor.objects.all().order_by("-id")[:5]
    total_instructors = all_instructors.count()
    class_schedules = ClassSchedule.objects.all()

    rooms = Room.objects.all()
    total_rooms = rooms.count()

    total_conflicts = sum(schedule.has_conflict() for schedule in class_schedules)
    total_schedules = class_schedules.count()
    return render(
        request,
        "dashboard.html",
        {
            "instructors": instructors,
            "class_schedules": class_schedules,
            "total_conflicts": total_conflicts,
            "total_rooms": total_rooms,
            "total_instructors": total_instructors,
            "total_schedules": total_schedules,
        },
    )


@login_required
def instructors(request):
    instructors = Instructor.objects.all().order_by("-id")
    # instructors = Instructor.objects.filter(role="User")
    paginator = Paginator(instructors, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "instructors.html",
        {"instructors": instructors, "page_obj": page_obj},
    )


@login_required
def schedule(request):
    instructors = Instructor.objects.all()
    class_schedules = ClassSchedule.objects.all()
    total_conflicts = sum(schedule.has_conflict() for schedule in class_schedules)
    return render(
        request,
        "schedule.html",
        {
            "instructors": instructors,
            "total_conflicts": total_conflicts,
        },
    )


@login_required
def section(request):
    if request.method == "POST":
        sectionform = SectionForm(request.POST, prefix="section")
        if sectionform.is_valid():
            program_section = sectionform.cleaned_data["program_section"]
            if Section.objects.filter(program_section=program_section).exists():
                messages.warning(request, "This section already exists")
            else:
                sectionform.save()
                messages.success(request, "Section Added")
            return redirect("section")
    else:
        sectionform = SectionForm(prefix="section")
    sections = Section.objects.all()
    return render(
        request,
        "section.html",
        {
            "sections": sections,
        },
    )


@login_required
def room(request):
    rooms = Room.objects.all().order_by("-id")
    room_events = []

    if request.method == "POST":
        roomform = RoomForm(request.POST, prefix="room")
        if roomform.is_valid():
            room_name = roomform.cleaned_data["room_name"]
            if Room.objects.filter(room_name=room_name).exists():
                messages.warning(request, "Room with this name already exists!")
            else:
                roomform.save()
                messages.success(request, "Room Added!")
            return redirect("room")
    else:
        roomform = RoomForm(prefix="room")

    for room in rooms:
        room_schedule = ClassSchedule.objects.filter(room=room)
        room_events_for_room = []

        for schedule in room_schedule:
            start_time = datetime.strptime(schedule.start_time, "%H:%M").strftime(
                "%H:%M:%S"
            )
            end_time = datetime.strptime(schedule.end_time, "%H:%M").strftime(
                "%H:%M:%S"
            )
            days_of_week_mapping = {
                "M": 1,
                "T": 2,
                "W": 3,
                "H": 4,
                "F": 5,
                "S": 6,
                "Sunday": 7,
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5,
                "Saturday": 6,
            }
            days_of_week = list(schedule.days_of_week)

            if days_of_week:
                event = {
                    "title": f"{schedule.course.course_name} - Mr/Mrs. {schedule.instructor.lastName} - {schedule.section}",
                    "daysOfWeek": [
                        days_of_week_mapping[day]
                        for day in days_of_week
                        if day in days_of_week_mapping
                    ],
                    "startTime": start_time,
                    "endTime": end_time,
                }
                room_events_for_room.append(event)

        room_events.append(
            {
                "room_name": room.room_name,
                "events": room_events_for_room,
                "college": room.college,
            }
        )
    schedules = ClassSchedule.objects.all()
    return render(
        request,
        "room.html",
        {
            "roomform": roomform,
            "rooms": rooms,
            "schedules": schedules,
            "room_events": room_events,
        },
    )


### Add Subjects ###
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


################# /// DELETE VIEWS /// ######################
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


def delete_schedule_section(request, id=None):
    instructor_course = InstructorCourse.objects.get(pk=id)

    section_to_delete_id = request.POST.get("section_id")
    if section_to_delete_id:
        try:
            section_to_delete = Section.objects.get(pk=section_to_delete_id)
            instructor_course.sections.remove(section_to_delete)
            messages.success(request, "Section Deleted!")
            if not instructor_course.sections.exists():
                instructor_course.delete()
                messages.success(
                    request, "Instructor course has no sections and is now removed."
                )
        except Section.DoesNotExist:
            messages.error(request, "Section not found.")
    else:
        messages.error(request, "Section not specified.")

    return redirect("editgenerate-schedule", id=instructor_course.instructor_id)


def delete_schedule_course(request, id=None):
    instructor_course = InstructorCourse.objects.get(id=id)
    instructor_course.delete()
    messages.success(request, "Successfully Deleted Course and its Section!")
    return redirect("editgenerate-schedule", id=instructor_course.instructor_id)


################# /// EDIT VIEWS ///######################
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


def update_schedule(request, id=None):
    schedules = {}
    schedule = get_object_or_404(ClassSchedule, id=id)
    course_choices = Course.objects.all()
    instructor_choices = Instructor.objects.all()
    room_choices = Room.objects.all()

    scheduleform = ClassScheduleForm(request.POST, instance=schedule)
    if scheduleform.is_valid():
        scheduleform.save()
        messages.success(request, "Schedule Updated!")
        return redirect("schedule")
    else:
        print(scheduleform.errors)

    scheduleform = ClassScheduleForm(instance=schedule)
    schedules["scheduleform"] = scheduleform
    return render(
        request,
        "schedule_update.html",
        {
            "scheduleform": scheduleform,
            "course_choices": course_choices,
            "instructor_choices": instructor_choices,
            "room_choices": room_choices,
        },
    )


def update_section(request, id=None):
    sections = {}
    section = get_object_or_404(Section, id=id)
    sectionform = SectionForm(request.POST, instance=section)
    if sectionform.is_valid():
        sectionform.save()
        messages.success(request, "Section Updated!")
        return redirect("section")

    sectionform = SectionForm(instance=section)
    sections["sectionform"] = sectionform
    return render(request, "section_update.html", sections)


def update_instructor(request, id=None):
    instructors = {}
    instructor = get_object_or_404(Instructor, id=id)
    instructor_courses = InstructorCourse.objects.filter(instructor=instructor)

    instructorform = InstructorForm(request.POST, request.FILES, instance=instructor)
    if instructorform.is_valid():
        instructorform.save()
        messages.success(request, "Instructor Updated!")
        return redirect("instructors")
    else:
        instructorform = InstructorForm(instance=instructor)

    instructors["instructorform"] = instructorform
    instructors["instructor_courses"] = instructor_courses
    return render(
        request,
        "instructor_update.html",
        instructors,
    )


def update_instructor_sections_courses(request, id=None):
    selected_instructor = Instructor.objects.get(id=id)
    instructors = {}
    instructor = get_object_or_404(Instructor, id=id)
    instructor_courses = InstructorCourse.objects.filter(instructor=instructor)

    instructorform = InstructorForm(request.POST, request.FILES, instance=instructor)

    if request.method == "POST":
        instructor_course_form = InstructorCourseForm(
            request.POST, prefix="instructor_course"
        )
        if instructor_course_form.is_valid():
            instructor_course_form.save()
            messages.success(request, "Section added to Instructor successfully.")
            return redirect("editgenerate-schedule", id=selected_instructor.id)
    else:
        instructor_course_form = InstructorCourseForm(prefix="instructor_course")

    instructors["instructorform"] = instructorform
    instructors["instructor_courses"] = instructor_courses

    return render(
        request,
        "generate_update.html",
        {
            "instructor_course_form": instructor_course_form,
            "sections": Section.objects.all(),
            "courses": Course.objects.all(),
            "instructors": Instructor.objects.all(),
            **instructors,
        },
    )


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


############## GENETIC ALGORITHM ########################
def generate_schedules(request):
    ### THIS WILL BE FIXED LATER ###
    # college = request.POST.get("college")
    # school_year = request.POST.get("schoolYear")
    # semester = request.POST.get("semester")

    valcollege = "CAS"
    valschool_year = "2020-2021"
    valsemester = "1st semester"
    print("Values are:", valcollege, valschool_year, valsemester)

    existing_schedule = ClassSchedule.objects.filter(
        year=valschool_year, semester=valsemester, instructor__college=valcollege
    ).exists()
    if existing_schedule:
        print("There is already an existing schedules")
        messages.warning(
            request,
            "A schedule with the same College, Semester and Year Level already exists.",
        )
        return redirect("generate-schedule")
    else:
        print("No existing schedules, Proceed")
        population = generate_population(300, valcollege, valschool_year, valsemester)
        best_individual = evolve(population, 300)

        class_schedules = best_individual.class_schedules
        context = {"class_schedules": class_schedules}

        messages.success(request, "Schedules Generated Successfully.")
    instructors = Instructor.objects.all()
    classSchedules = ClassSchedule.objects.all()
    total_conflicts = sum(schedule.has_conflict() for schedule in classSchedules)
    return render(
        request,
        "schedule.html",
        {
            "instructors": instructors,
            **context,
            "classSchedules": classSchedules,
            "total_conflicts": total_conflicts,
        },
    )


def sampleTest(request):
    if request.method == "POST":
        college = request.POST.get("college")
        school_year = request.POST.get("schoolYear")
        semester = request.POST.get("semester")

        # Write values to a file
        passValue = viewData(college, school_year, semester)
        # print(college, school_year, semester)

        return JsonResponse({"message": "Values passed successfully."})
    else:
        print("Nothing passed")

    return JsonResponse({"error": "Invalid request."}, status=400)
