from sqlalchemy.orm import relationship

from models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class Brand(BaseModel):
    __tablename__ = "brands"

    name = Column(String(35), unique=True, nullable=False)


class Model(BaseModel):
    __tablename__ = "models"

    name = Column(String(35), nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("Brand")
