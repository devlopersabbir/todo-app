from typing import Optional
from pydantic import BaseModel


class TodoSchema(BaseModel):
    name: str
    description: str
    isDone: str
