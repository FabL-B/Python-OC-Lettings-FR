Quick Start Guide
=================

This guide provides the essential steps to quickly run the OC Lettings Site application locally.

1. Clone the repository
-----------------------
.. code-block:: bash

    git clone https://github.com/FabL-B/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

2. Create and activate a virtual environment
--------------------------------------------

**With venv :**

.. code-block:: bash

    python -m venv env
    .\env\Scripts\activate     # Windows
    source env/bin/activate    # macOS/Linux

**Or with pipenv :**

.. code-block:: bash

    pip install pipenv
    pipenv shell

3. Install dependencies
-----------------------

.. code-block:: bash

    pip install -r requirements.txt

4. Apply migrations
-------------------

.. code-block:: bash

    python manage.py migrate

5. Create a superuser (admin)
-----------------------------

.. code-block:: bash

    python manage.py createsuperuser

6. Run the development server
-----------------------------

.. code-block:: bash

    python manage.py runserver

The application will be available at the following address:

http://127.0.0.1:8000/
