from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(max_length=1000, default=None)
    completed: bool = False
    due_date: datetime
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    user_id: int
    due_date: datetime | None = None