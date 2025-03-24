Deployment of the Application
=============================

This document describes the deployment steps for the OC Lettings Site project.

Hosting
-------

The application is hosted on the Render platform, a simple and efficient cloud service for hosting Dockerized applications.

CI/CD Pipeline
--------------

The deployment is fully automated through a CI/CD pipeline based on GitHub and Docker. It includes three steps:

1. **Testing and linting**
   - Run tests using `pytest`
   - Analyze code using `flake8`
   - Test coverage must be above 80%

2. **Containerization**
   - Build a Docker image of the project
   - Push this image to **Docker Hub**
   - Tag the image with the commit hash

3. **Deployment**
   - Deployment is automatically triggered **only** when the `master` branch is updated.
   - The site is deployed using the built Docker image.

Trigger Conditions
------------------

- **Branches other than `master`** :
  - Only tests and linting are executed
  - No Docker build, no deployment

- **`master` branch** :
  - Full pipeline execution: tests → Docker → deployment

Docker Configuration
--------------------

The project includes a  `Dockerfile` at the root. Example command to test locally:

.. code-block:: bash

    docker build -t oclettings .
    docker run -p 8000:8000 oclettings

Render Configuration
--------------------

In the Render interface:

- Create a **Web Service** using Docker
- Provide the GitHub repository URL
- Add the required environment variables in the dashboard:
  - `SECRET_KEY`
  - `DEBUG`
  - `SENTRY_DSN` (if used)

Error Logging with Sentry
-------------------------

The project integrates **Sentry** for monitoring errors in production.

Steps:

1. Install the Python SDK
2. Configure it in `settings.py`
3. Use the `logging` module to generate logs
4. Never include the DSN key directly in the code (use environment variables)

Documentation Update
--------------------

Each time the repository is updated, the documentation is automatically rebuilt using **Read the Docs**.

