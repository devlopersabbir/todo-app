import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.loadEnv import loadEnv
loadEnv()

DATABSE_URL = os.environ.get("DATABSE_URL")
if not DATABSE_URL:
    print("Fail to get DATABASE URL!")

engine = create_engine(DATABSE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
