from sqlalchemy.orm import Session
from db_models import User, Task
from models import UserCreate, TaskCreate
from typing import List, Optional
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== USER CRUD =====

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = pwd_context.hash(user.password)  
    
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    
    db.add(db_user)        
    db.commit()            
    db.refresh(db_user)    
    return db_user

def get_user_by_email(db: Session, email: str) -> User | None:  
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db=db, email=email)  
    
    if not user:
        return None
    
    if not pwd_context.verify(password, user.hashed_password):
        return None
        
    return user

# ===== TASK CRUD =====

def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        due_date=task.due_date if hasattr(task, 'due_date') else None,  
        user_id=user_id 
    )
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_update: TaskCreate) -> Task | None:
    db_task = get_task_by_id(db, task_id)
    
    if not db_task:
        return None
    
    db_task.title = task_update.title
    db_task.description = task_update.description
    db_task.completed = task_update.completed
    if hasattr(task_update, 'due_date'):  
        db_task.due_date = task_update.due_date
    
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> bool:
    db_task = get_task_by_id(db, task_id)
    
    if not db_task:
        return False
    
    db.delete(db_task)
    db.commit()
    return True

# ===== HELPER FUNCTIONS =====

def get_user_by_username(db: Session, username: str) -> User | None:
    """Función extra por si necesitas buscar por username"""
    return db.query(User).filter(User.username == username).first()

def check_email_exists(db: Session, email: str) -> bool:
    """Verificar si email ya existe antes de crear usuario"""
    return db.query(User).filter(User.email == email).first() is not None

def check_username_exists(db: Session, username: str) -> bool:
    """Verificar si username ya existe antes de crear usuario"""
    return db.query(User).filter(User.username == username).first() is not None