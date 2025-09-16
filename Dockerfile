FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "echo '⏳ Esperando a PostgreSQL...' && sleep 10 && echo '🏗️ Creando tablas...' && python create_tables.py && echo '🚀 Iniciando servidor...' && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]