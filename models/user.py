from models.base import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(20), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
