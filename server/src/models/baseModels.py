import uuid
from src.configs.databse import Base
from sqlalchemy import Column, Integer, String, DateTime
import datetime


class BaseModels(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, unique=True, index=True)
    uuid = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))

    create_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(),
                        onupdate=datetime.datetime.now())
