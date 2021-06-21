from sqlalchemy import select

from models.car import Brand, Model
from services.base import BaseService


class BrandService(BaseService):
    model = Brand

    async def get_brand(self, brand_id: int):
        result = await self.db.execute(
            select(self.model).filter(self.model.id == brand_id)
        )
        return result.one()

    async def get_brands(self):
        result = await self.db.execute(
            select(self.model)
        )
        return result.scalars().all()


class ModelService(BaseService):
    model = Model

    async def get_model(self, model_id: int):
        result = await self.db.execute(
            select(self.model).filter(self.model.id == model_id)
        )
        return result.one()

    async def get_models(self, brand_id: int):
        result = await self.db.execute(
            select(self.model).filter_by(brand_id=brand_id)
        )
        return result.scalars().all()
