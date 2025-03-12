from django.urls import path
from profiles import views

"""
URL configuration module for the Profiles application.

This module defines the routes for displaying the list of user profiles
and the details of a specific profile.
"""

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile_detail, name="profile_detail"),
]
