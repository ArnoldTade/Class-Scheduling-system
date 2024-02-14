from django.urls import path
from class_sched import views


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("instructors/", views.instructors, name="instructors"),
    path("schedule/", views.schedule, name="schedule"),
    path("subject/", views.subject, name="subject"),
    path("home/", views.home, name="home"),
    # For user Login
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    # Delete
    path("deletesubject/<int:id>", views.delete_subject, name="deletesubject"),
    path("deleteroom/<int:id>", views.delete_room, name="deleteroom"),
    # Update
    path("edit/<int:id>", views.update_subject, name="edit"),
]
