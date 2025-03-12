from django.shortcuts import render

"""
View management module for the OC Lettings Site application.

This module contains the main view for rendering the home page.
"""


def index(request):
    """
    Display the homepage.
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Display 404 error.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Display 500 error.
    """
    return render(request, "500.html", status=500)
