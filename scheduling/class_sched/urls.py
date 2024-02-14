from django.urls import path
from class_sched import views
from django.conf import settings
from django.conf.urls.static import static

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
    path("deleteinstructor/<int:id>", views.delete_instructor, name="deleteinstructor"),
    # Update
    path("edit/<int:id>", views.update_subject, name="edit"),
    path("editinstructor/<int:id>", views.update_instructor, name="editinstructor"),
    path("editprofile/<int:id>", views.profile_edit, name="editprofile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
