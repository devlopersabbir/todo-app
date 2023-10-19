from sqlalchemy import Column, String, Boolean
from src.models.baseModels import BaseModels


class Todo(BaseModels):
    __tablename__ = "Todos"

    name = Column(String(256), unique=True)
    isDone = Column(Boolean(), default=False)
