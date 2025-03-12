from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

"""
Data models module for the Lettings application.

This module contains the Address and Letting models used to store
rental information and associated addresses.
"""


class Address(models.Model):
    """
    Model representing a postal address.

    Attributes:
        number (int): Street number.
        street (str): Street name.
        city (str): City of the address.
        state (str): Two-letter state code.
        zip_code (int): Postal code.
        country_iso_code (str): Three-letter ISO country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model representing a rental property.

    Attributes:
        title (str): Title of the rental.
        address (Address): Associated address of the rental.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
