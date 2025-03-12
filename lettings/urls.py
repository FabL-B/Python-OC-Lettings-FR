from django.urls import path
from lettings import views

"""
URL configuration module for the Lettings application.

This module defines the routes for displaying the list of rentals
and the details of a specific rental.
"""

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting_detail, name="letting_detail"),
]
