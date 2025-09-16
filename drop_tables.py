from database import engine
from db_models import Base

Base.metadata.drop_all(bind=engine)
print("✅ Tablas eliminadas exitosamente!")