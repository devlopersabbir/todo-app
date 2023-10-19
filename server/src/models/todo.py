from sqlalchemy import Column, String, Boolean, Text
from src.models.baseModels import BaseModels


class Todo(BaseModels):
    __tablename__ = "Todos"

    name = Column(String(256), unique=True, nullable=False)
    description = Column(String(Text))
    isDone = Column(Boolean(), default=False)
