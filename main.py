from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import UserCreate, UserResponse, TaskCreate, TaskResponse
from database import get_db
from db_models import User, Task
import crud
from typing import List

app = FastAPI(
    title="Task Manager API",
    description="API para gestión de tareas con PostgreSQL",
    version="1.0.0"
)

# Endpoints
@app.get("/")
async def welcome():
    return {"message": "Bienvenido/a a Task Manager API"}

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.check_email_exists(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = crud.create_user(db=db, user=user)
    
    return UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email,
        created_at=new_user.created_at
    )

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        created_at=user.created_at
    )

@app.post("/users/{user_id}/tasks/", response_model=TaskResponse)
async def create_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = crud.create_task(db=db, task=task, user_id=user_id)
    return TaskResponse(
        id=new_task.id,
        title=new_task.title,
        description=new_task.description,
        completed=new_task.completed,
        created_at=new_task.created_at,
        user_id=new_task.user_id,
        due_date=new_task.due_date
    )

@app.get("/users/{user_id}/tasks/", response_model=List[TaskResponse])
async def get_user_tasks(user_id: int, db: Session = Depends(get_db)):  # ← Corregido: user_id
    # Verificar que el usuario existe
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    tasks = crud.get_tasks_by_user(db, user_id)
    
    task_responses = []
    for task in tasks:
        task_responses.append(TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            completed=task.completed,
            created_at=task.created_at,
            user_id=task.user_id,
            due_date=task.due_date
        ))
    return task_responses

@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=task.created_at,
        user_id=task.user_id,
        due_date=task.due_date
    )

@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task_update)
    
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskResponse(
        id=updated_task.id,
        title=updated_task.title,
        description=updated_task.description,
        completed=updated_task.completed,
        created_at=updated_task.created_at,
        user_id=updated_task.user_id,
        due_date=updated_task.due_date
    )

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": f"Task {task_id} deleted successfully"}

# Endpoints extras útiles
@app.get("/users/", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    """Obtener todos los usuarios (útil para testing)"""
    users = db.query(User).all()
    return [UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        created_at=user.created_at
    ) for user in users]

@app.get("/tasks/", response_model=List[TaskResponse])
async def get_all_tasks(db: Session = Depends(get_db)):
    """Obtener todas las tareas (útil para testing)"""
    tasks = db.query(crud.Task).all()
    return [TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=task.created_at,
        user_id=task.user_id,
        due_date=task.due_date
    ) for task in tasks]