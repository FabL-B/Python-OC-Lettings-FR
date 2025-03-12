from django.urls import path
from lettings import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting_detail, name="letting_detail"),
]