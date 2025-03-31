from django.shortcuts import render
from profiles.models import Profile
import logging
from django.http import Http404

"""
View management module for the Profiles application.

This module contains views to display the list of user profiles
and details of a specific profile.
"""

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of user profiles.
    """
    logger.info("[Profiles] Viewing list of profiles")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile_detail(request, username):
    """
    Display details of a specific user profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"[Profiles] Profile found: {profile}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f"[Profiles] No profile found with ID={username}")
        raise Http404("Profile not found")
