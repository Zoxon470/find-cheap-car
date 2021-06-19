from fastapi import APIRouter

from providers import providers
from schemas.search import Query

router = APIRouter()


@router.post("/search")
async def search(query: Query):
    result = []
    for provider in providers:
        result.append(await provider.job(query=query))
    return {"result": result}
