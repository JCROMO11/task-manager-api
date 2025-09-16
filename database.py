import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Detectar entorno
env_type = os.getenv("APP_ENV", "local")

# Configuración de base de datos
if env_type == "docker":
    DATABASE_URL = os.getenv("DATABASE_URL_DOCKER", "postgresql+psycopg2://task_user:taskpassword123@db:5432/task_manager_db")
else:
    DATABASE_URL = os.getenv("DATABASE_URL_LOCAL", "postgresql+psycopg2://task_user:taskpassword123@localhost:5433/task_manager_db")

print(f"🔗 Conectando a: {DATABASE_URL.replace('taskpassword123', '***')}")

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