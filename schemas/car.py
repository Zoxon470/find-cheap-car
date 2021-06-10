from pydantic import BaseModel


class Model(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
