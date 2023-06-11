# Define la imagen base con la versión de Node deseada
FROM node:18.16.0

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo package.json y package-lock.json al contenedor
COPY package*.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia el contenido del proyecto al contenedor
COPY . .

# Compila la aplicación React
RUN npm run build

# Expone el puerto que utilizará la aplicación
EXPOSE 3000

# Comando para ejecutar la aplicación React
CMD ["npm", "run", "dev"]
