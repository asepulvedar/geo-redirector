# Usa la imagen oficial de Python
FROM python:3.10-slim

# Define el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y la app al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto
EXPOSE 8080

# Comando para ejecutar la app
CMD ["python", "app.py"]