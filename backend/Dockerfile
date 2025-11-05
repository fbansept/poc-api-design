# Utilise l'image officielle Node.js 25
FROM node:25

# Définit le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copie les fichiers package.json et package-lock.json
COPY package*.json ./
COPY app.js ./

# Installe les dépendances
RUN npm install

CMD node app.js