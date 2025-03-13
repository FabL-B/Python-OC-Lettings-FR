import logging
from django.shortcuts import render
from lettings.models import Letting

"""
View management module for the Lettings application.

This module contains views to display the list of rentals
and details of a specific rental.
"""

logger = logging.getLogger(__name__)

def index(request):
    """
    Display the list of available rentals.
    """
    logger.info("[Lettings] Viewing list of rentals")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting_detail(request, letting_id):
    """
    Display details of a specific rental.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"[Lettings] Rental found: {letting.title}")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"[Lettings] No rental found with ID={letting_id}")
        return render(request, '404.html', status=404)
