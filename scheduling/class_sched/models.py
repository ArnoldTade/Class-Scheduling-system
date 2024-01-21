from django.db import models


# Create your models here.
class Faculty(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
