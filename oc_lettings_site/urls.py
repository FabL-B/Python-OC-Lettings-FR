from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from oc_lettings_site.views import custom_404, custom_500, index

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
]
