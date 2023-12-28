from django.db import models


# Create your models here.
class Faculty(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
