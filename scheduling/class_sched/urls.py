from django.urls import path
from class_sched import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("instructors/", views.instructors, name="instructors"),
    path("schedule/", views.schedule, name="schedule"),
    path("about/", views.about, name="about"),
    path("home/", views.home, name="home"),
]
