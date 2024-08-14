from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session as OrmSession
from sqlmodel import select
from typing import List
from uuid import UUID
from database.database import create_db_and_tables, get_session
from models.response_models import ResponseModel, ErrorResponseModel
from models.todo import Todo
from models.todo import TodoCreate
from models.todo import TodoUpdate

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/todos/", response_model=ResponseModel)
def get_todos(session: OrmSession = Depends(get_session)):
    result = session.execute(select(Todo))
    todos = result.scalars().all()
    return ResponseModel(status="Success", message="Fetched all todos", data=todos)

@app.post("/todos/", response_model=ResponseModel)
def create_todo(todo_create: TodoCreate, session: OrmSession = Depends(get_session)):
    todo = Todo(**todo_create.dict())
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return ResponseModel(status="Success", message="Todo created successfully", data=todo)


@app.get("/todos/{todo_id}", response_model=ResponseModel)
def get_todo_by_id(todo_id: UUID, session: OrmSession = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=ErrorResponseModel(status="Error", message="Todo not found").dict())
    return ResponseModel(status="Success", message="Fetched todo by ID", data=todo)

@app.put("/todos/{todo_id}", response_model=ResponseModel)
def update_todo(todo_id: UUID, updated_todo: TodoUpdate, session: OrmSession = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=ErrorResponseModel(status="Error", message="Todo not found").dict())
    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.status = updated_todo.status
    session.commit()
    session.refresh(todo)
    return ResponseModel(status="Success", message="Todo updated successfully", data=todo)

@app.delete("/todos/{todo_id}", response_model=ResponseModel)
def delete_todo(todo_id: UUID, session: OrmSession = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=ErrorResponseModel(status="Error", message="Todo not found").dict())
    session.delete(todo)
    session.commit()
    return ResponseModel(status="Success", message="Todo deleted successfully", data=todo)

@app.patch("/todos/{todo_id}/status", response_model=ResponseModel)
def update_todo_status(todo_id: UUID, session: OrmSession = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail=ErrorResponseModel(status="Error", message="Todo not found").dict())

    if todo.status == "completed":
        todo.status = "pending"
    else:
        todo.status = "completed"

    session.commit()
    session.refresh(todo)
    return ResponseModel(status="Success", message="Todo status updated successfully", data=todo)
