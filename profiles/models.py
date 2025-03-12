from django.db import models
from django.contrib.auth.models import User

"""
Data models module for the Profiles application.

This module contains the Profile model, which extends user-related data.
"""


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (User): The associated Django User.
        favorite_city (str): The user's favorite city (optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
