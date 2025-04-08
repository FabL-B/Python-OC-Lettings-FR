import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting
from sentry_sdk import capture_exception

"""
View management module for the Lettings application.

This module contains views to display the list of rentals
and details of a specific rental.
"""

logger = logging.getLogger("django")


def index(request):
    """
    Display the list of available rentals.
    """
    try:
        logger.info("[Lettings] Viewing list of rentals")
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(
            "[Lettings] Error while listing rentals",
            exc_info=e
            )
        capture_exception(e)
        raise


def letting_detail(request, letting_id):
    """
    Display details of a specific rental.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(f"[Lettings] Rental found: {letting.title}")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(
            f"[Lettings] Error while retrieving rental ID={letting_id}",
            exc_info=e
            )
        capture_exception(e)
        raise
