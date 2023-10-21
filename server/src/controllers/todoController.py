from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.models.todo import Todo
from src.schemas.todoSchema import TodoSchema


def index_todo(db: Session):
    isTodo = db.query(Todo).all()
    if isTodo:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=isTodo
        )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": "No todo found!"
        }
    )


def store_todo(db: Session, todo: TodoSchema):
    try:
        db_todo = Todo(
            name=todo.name,
            description=todo.description,
            isDone=todo.isDone
        )
        db.add(db_todo)
        db.commit()
        db.refresh()

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=db_todo
        )
    except Exception as err:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Something went wrong!",
                "error": str(err)
            }
        )
