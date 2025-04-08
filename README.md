## Table of Contents

- [Summary](#summary)
- [Local Development](#local-development)
  - [macOS / Linux](#macos--linux)
  - [Windows](#windows)
- [Documentation](#documentation)
- [Technologies Used](#technologies-used)

## Summary

Orange County Lettings website

**Online access**: [https://oc-lettings-site-flb.onrender.com](https://oc-lettings-site-flb.onrender.com)

**Documentation**: [https://python-oc-lettings-fr-flb.readthedocs.io/en/latest/](https://python-oc-lettings-fr-flb.readthedocs.io/en/latest/)

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed that the `python` command from your OS shell runs the above-mentioned Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/FabL-B/Python-OC-Lettings-FR`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step throws a "package not found" error on Ubuntu)
- Activate the environment: `source venv/bin/activate`
- Confirm that the `python` command runs the Python interpreter from the virtual environment  
  `which python`
- Confirm that the Python interpreter version is 3.6 or higher  
  `python --version`
- Confirm that the `pip` command runs the pip executable from the virtual environment  
  `which pip`
- To deactivate the environment: `deactivate`

#### Run the site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm that the site works and is navigable (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a shell session: `sqlite3`
- Connect to the database: `.open oc-lettings-site.sqlite3`
- Display the tables in the database: `.tables`
- Display the columns in the profile table: `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profile table:  
  `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Log in with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, same as above except:

- To activate the virtual environment: `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Documentation

The technical documentation of the project is generated with [Sphinx](https://www.sphinx-doc.org/) and hosted on [Read the Docs](https://readthedocs.org/).

It includes:

- An installation and deployment guide
- A description of the technologies used
- Manual documentation for models and views
- (Optional) An automatically generated API reference using `autodoc`

Access the documentation: [https://python-oc-lettings-fr-flb.readthedocs.io/en/latest/](https://python-oc-lettings-fr-flb.readthedocs.io/en/latest/)

To regenerate the documentation locally:

```bash
# On Windows
.\docs\make.bat html

# On Linux/macOS
make html

# Open local documentation
docs/build/html/index.html
```

## Technologies Used

- Python 3.12
- Django 4.x
- SQLite
- Docker & DockerHub
- Render (hébergement)
- GitHub & GitHub Actions
- Sphinx + Read the Docs
