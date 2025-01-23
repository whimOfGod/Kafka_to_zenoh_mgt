FROM python:3.9-slim

# Définir le répertoire de travail à la racine du projet (au lieu de /app)
WORKDIR /

# Copier les fichiers dans le conteneur en respectant la structure actuelle
COPY eNDBF eNDBF
COPY FLAD FLAD
COPY INDBF INDBF
COPY NDPPF NDPPF

# Installer les dépendances pour chaque composant
RUN pip install --upgrade pip && \
    pip install -r eNDBF/requirements.txt && \
    pip install -r FLAD/FLClient/requirements.txt && \
    pip install -r FLAD/FLInference/requirements.txt && \
    pip install -r FLAD/FLServer/requirements.txt && \
    pip install -r INDBF/requirements.txt && \
    pip install -r NDPPF/requirements.txt

CMD ["tail", "-f", "/dev/null"]
