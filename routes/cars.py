from typing import List

from fastapi import APIRouter, Depends

from database.config import get_db
from schemas.car import Model
from services.car import ModelService

router = APIRouter()


@router.get("/get-models", response_model=List[Model])
async def get_models(brand_id: int, db=Depends(get_db)):
    brands = await ModelService(db).get_models(brand_id)
    return brands
