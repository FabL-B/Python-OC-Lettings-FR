Data Models
===========

This section describes the main data models used in the application.

Address Model
-------------

This model represents a full postal address, used in lettings.

**Fields**:

- `number` (int): Street number  
- `street` (str): Street name  
- `city` (str): City  
- `state` (str): State (2 letters)  
- `zip_code` (int): Zip code  
- `country_iso_code` (str): Country ISO code (e.g., FR, US)

**Usage example**:

.. code-block:: python

    address = Address.objects.create(
        number=12,
        street="Rue de la République",
        city="Lyon",
        state="FR",
        zip_code=69000,
        country_iso_code="FR"
    )

Letting Model
-------------

This model represents a letting, linked to an address.

**Fields**:

- `title` (str): Letting title  
- `address` (ForeignKey to Address): Associated address

**Usage example**:

.. code-block:: python

    from lettings.models import Address, Letting

    address = Address.objects.create(
        number=42,
        street="Boulevard Haussmann",
        city="Paris",
        state="FR",
        zip_code=75009,
        country_iso_code="FR"
    )

    letting = Letting.objects.create(
        title="Appartement Haussmannien",
        address=address
    )


Profile Model
-------------

Extension of the default Django user model. Each profile is linked to one user.

**Fields**:

- `user` (OneToOneField to User): Linked Django user  
- `favorite_city` (str): User's favorite city

**Usage example**:

.. code-block:: python

    from django.contrib.auth.models import User
    from profiles.models import Profile

    user = User.objects.create_user(username="jean", password="motdepasse123")

    profile = Profile.objects.create(
        user=user,
        favorite_city="Bordeaux"
    )
