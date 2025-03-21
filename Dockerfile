# Utilise une image Python officielle comme base
FROM python:3.10

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers du projet
COPY . /app

# Installation des dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collecte des fichiers statiques Django
RUN python manage.py collectstatic --noinput

# Port exposé
EXPOSE 8000

# Commande de démarrage (avec gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]