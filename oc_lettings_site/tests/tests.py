import pytest
from django.test import override_settings
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client):
    """Test home page."""
    response = client.get(reverse("index"))

    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_custom_404_page(client):
    """Test custom 404 error page."""
    response = client.get("/unknown-page/")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@override_settings(DEBUG=False)
def test_custom_500_page(client):
    """Test custom 500 error page uses 500.html template."""
    client.raise_request_exception = False
    response = client.get("/trigger-500/")

    assert response.status_code == 500
    assertTemplateUsed(response, "500.html")
