from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
import logging
from sentry_sdk import capture_exception

"""
View management module for the Profiles application.

This module contains views to display the list of user profiles
and details of a specific profile.
"""

logger = logging.getLogger("django")


def index(request):
    """
    Display the list of user profiles.
    """
    try:
        logger.info("[Profiles] Viewing list of profiles")
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(
            "[Profiles] Error while listing profiles",
            exc_info=e
            )
        raise


def profile_detail(request, username):
    """
    Display details of a specific user profile.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"[Profiles] Profile found: {profile}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(
            f"[Profiles] Error while retrieving profile: username={username}",
            exc_info=e
            )
        raise
