from sqlmodel import SQLModel
from typing import List, Optional, Union
from uuid import UUID
from models.todo import Todo

class ResponseModel(SQLModel):
    status: str
    message: str
    data: Optional[Union[Todo, List[Todo]]] = None

class ErrorResponseModel(SQLModel):
    status: str
    message: str
