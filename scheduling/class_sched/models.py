from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.


class Instructor(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="img/", null=True, default="img/placeholder.png"
    )
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    course_handled = models.ManyToManyField(
        "Course", blank=True, through="InstructorCourse"
    )

    def __str__(self):
        return f"{self.lastName}, {self.firstName} "


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.CharField(max_length=100)
    hours = models.IntegerField()
    prerequisites = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class ClassSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    year = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def has_conflict(self):
        conflicts = ClassSchedule.objects.filter(
            days_of_week=self.days_of_week,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
            room=self.room,
            semester=self.semester,
            year=self.year,
        ).exclude(pk=self.pk)

        return conflicts.count()

    def __str__(self):
        return f"{self.instructor}, {self.course}, {self.section}, {self.room} "


class Week(models.Model):
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.day


class Section(models.Model):
    program_section = models.CharField(max_length=100)
    section_college = models.CharField(max_length=100)
    section_major_course = models.CharField(max_length=100)
    number_students = models.IntegerField()

    def __str__(self):
        return self.program_section


class InstructorCourse(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.instructor} - {self.course} - {self.section}"
