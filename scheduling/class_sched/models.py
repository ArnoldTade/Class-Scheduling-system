from django.db import models

# Create your models here.


class Instructor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    time_availability = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="img/")
    role = models.CharField(max_length=100)


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
