from django.db import models
from django.contrib.auth.models import User

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


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)


class ClassSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    year = models.CharField(max_length=100)

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


class Conflict(models.Model):
    schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    details = models.TextField()


class Feedback(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    content = models.TextField()
