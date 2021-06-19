from pydantic import BaseModel, HttpUrl


class Query(BaseModel):
    brand: str
    model: str


class SearchResult(BaseModel):
    url: HttpUrl
    price: str
    image: HttpUrl
