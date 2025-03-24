import pytest
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

# faire test de erreur 500
