from database import engine
from db_models import Base

Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente!")