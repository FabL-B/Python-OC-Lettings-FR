import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains
from lettings.models import Address, Letting


