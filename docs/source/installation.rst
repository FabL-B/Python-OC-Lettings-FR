Project Installation
====================

This guide explains how to install and run the OC Lettings Site project locally.

Prerequisites
-------------

Make sure you have the following installed on your machine:

- Python 3.8 ou higher
- pip (comes with Python)
- Git
- A virtual environment

Clone the repository
--------------------

Open a terminal and run the following command:

.. code-block:: bash

    git clone https://github.com/FabL-B/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

Create a virtual environment
----------------------------

With venv:

.. code-block:: bash

    python -m venv env
    source env/bin/activate    # Linux/macOS
    .\env\Scripts\activate     # Windows

Or with pipenv:

.. code-block:: bash

    pip install pipenv
    pipenv shell

Install dependencies
--------------------

.. code-block:: bash

    pip install -r requirements.txt

Apply database migrations
-------------------------

.. code-block:: bash

    python manage.py migrate

Create a superuser
------------------

.. code-block:: bash

    python manage.py createsuperuser

Run the local server
--------------------

.. code-block:: bash

    python manage.py runserver

The application will be available at: http://127.0.0.1:8000/

Run the tests
-------------

To run the unit and integration tests, use:

.. code-block:: bash

    pytest

Code style check (optional)
---------------------------

To check that your code follows the style guide:

.. code-block:: bash

    flake8


Admin panel access (optional)
-----------------------------

You can log into the Django admin interface at:

http://127.0.0.1:8000/admin

Use the credentials you created with the `createsuperuser` command.
