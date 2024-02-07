from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Instructor(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.TextField()
    department = models.CharField(max_length=100)
    time_availability = models.CharField(max_length=100)
    role = models.CharField(
        max_length=100, choices=(("admin", "Admin"), ("user", "User"))
    )


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100)


class ClassSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    days_of_week = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()


class InstructorSchedule(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)


class Conflict(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    details = models.TextField()


class Feedback(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    content = models.TextField()
