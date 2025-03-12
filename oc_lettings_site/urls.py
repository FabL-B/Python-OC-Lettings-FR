from django.contrib import admin
from django.urls import path, include

from oc_lettings_site.views import index

"""
URL configuration module for the OC Lettings Site application.

This module defines the main URL routes of the application, including
index handling and app-specific URL configurations.
"""


handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
]
