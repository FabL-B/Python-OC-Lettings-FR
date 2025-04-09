from django.shortcuts import render
from sentry_sdk import capture_exception
import logging

"""
View management module for the OC Lettings Site application.

This module contains the main view for rendering the home page.
"""

logger = logging.getLogger("django")


def index(request):
    """
    Display the homepage.
    """
    logger.info("Homepage accessed")
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Display 404 error and capture it in Sentry.
    """
    capture_exception(exception)
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Display 500 error and capture it in Sentry.
    """
    capture_exception()
    return render(request, "500.html", status=500)


def trigger_500(request):
    """
    Simulated view used only to test the 500 error handler.
    """
    raise Exception("Test 500 error")
