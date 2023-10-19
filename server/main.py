from fastapi import FastAPI
from src.configs.db_connect import db_connect

db_connect()
app = FastAPI()

# health checking


@app.get("/")
def root():
    return {
        "hello": "world"
    }
