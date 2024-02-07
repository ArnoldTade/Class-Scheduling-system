from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Room)
admin.site.register(Course)
admin.site.register(ClassSchedule)
admin.site.register(InstructorSchedule)
admin.site.register(Conflict)
admin.site.register(Feedback)
