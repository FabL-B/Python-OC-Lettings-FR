from django.shortcuts import render
from profiles.models import Profile

"""
View management module for the Profiles application.

This module contains views to display the list of user profiles
and details of a specific profile.
"""


def index(request):
    """
    Display the list of user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile_detail(request, username):
    """
    Display details of a specific user profile.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
