from django.urls import path
from class_sched import views


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("instructors/", views.instructors, name="instructors"),
    path("schedule/", views.schedule, name="schedule"),
    path("about/", views.about, name="about"),
    path("home/", views.home, name="home"),
    # For user Login
]
