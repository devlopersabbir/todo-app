from sqlalchemy import Column, String, Boolean
from src.models.baseModels import BaseModels


class Todo(BaseModels):
    __tablename__ = "Todos"

    name = Column(String(256), unique=True, nullable=False)
    description = Column(String(256), nullable=False)
    isDone = Column(Boolean(), nullable=True, default=False)
