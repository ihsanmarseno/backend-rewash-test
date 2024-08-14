from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID
from typing import Optional
from pydantic import BaseModel

class Todo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str = Field(default="pending")

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

class TodoUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
