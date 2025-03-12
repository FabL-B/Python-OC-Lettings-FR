from django.shortcuts import render
from lettings.models import Letting

"""
View management module for the Lettings application.

This module contains views to display the list of rentals
and details of a specific rental.
"""


def index(request):
    """
    Display the list of available rentals.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting_detail(request, letting_id):
    """
    Display details of a specific rental.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
