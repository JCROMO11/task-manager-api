import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Detectar entorno
env_type = os.getenv("APP_ENV", "local")

# NUEVO: Railway environment handling
if env_type == "docker":
    # Primero intentar DATABASE_URL (Railway), después fallback local
    DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("DATABASE_URL_DOCKER")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")

print(f"🔗 Conectando a: {DATABASE_URL.replace('password', '***') if DATABASE_URL else 'No DATABASE_URL'}")

# Configuración SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()