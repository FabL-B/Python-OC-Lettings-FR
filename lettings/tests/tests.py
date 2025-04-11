import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains
from lettings.models import Address, Letting
from profiles.views import profile_detail


@pytest.mark.django_db
def test_index_view(client):
    """Test lettings index page."""
    response = client.get(reverse("lettings:index"))

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_view(client):
    """Test letting detail page."""
    address = Address.objects.create(
        number=10, street="Main Street", city="New York",
        state="NY", zip_code=10001, country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Nice Apartment", address=address)

    response = client.get(
        reverse("lettings:letting_detail", args=[letting.id])
    )

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    assertContains(response, "Nice Apartment")


@pytest.mark.django_db
def test_letting_detail_view_invalid_id(client):
    """Test letting detail page for a non-existent letting returns 404."""
    response = client.get(reverse("lettings:letting_detail", args=[999]))
    assert response.status_code == 404
