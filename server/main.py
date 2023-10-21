from fastapi import FastAPI
from src.configs.db_connect import db_connect
from src.routes import todoRoutes

app = FastAPI()
db_connect()


app.include_router(router=todoRoutes.router, prefix="/api/v1/todos")


# health checking


@app.get("/")
def root():
    return {
        "hello": "world"
    }
