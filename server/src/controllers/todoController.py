from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.models.todo import Todo


def index_todo(db: Session):
    isTodo = db.query(Todo).all()
    print(isTodo)
    if isTodo:
        JSONResponse(
            status_code=status.HTTP_200_OK,
            content=isTodo
        )
    JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": "No todo found!"
        }
    )
