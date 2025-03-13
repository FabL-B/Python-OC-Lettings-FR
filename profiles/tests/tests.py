import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    """Test profiles index page."""
    response = client.get(reverse("profiles:index"))

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test profile detail page."""
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="Nantes")

    response = client.get(reverse("profiles:profile_detail", args=["testuser"]))

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
    assertContains(response, "Nantes")
