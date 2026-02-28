from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("comments/", views.comments, name="comments"),
    path("profile/", views.profile, name="profile"),path("profile/", views.profile, name="profile"),
]
