from httpx import AsyncClient
from pydantic import HttpUrl

from schemas.search import Query, SearchResult


class AbstractProvider:
    def __init__(
            self,
            name: str,
            url: HttpUrl,
            http_client: AsyncClient = AsyncClient
    ):
        self.name = name
        self.url = url
        self.http_client = http_client

    async def job(self, query: Query): ...

    def result(self, **kwargs) -> SearchResult:
        return SearchResult(**kwargs)
