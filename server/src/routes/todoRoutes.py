from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controllers.todoController import index_todo
from src.configs.databse import get_db


router = APIRouter()


@router.get("/", tags=["GET TODOS"])
async def get_todo(db: Session = Depends(get_db)):
    return index_todo(db)
