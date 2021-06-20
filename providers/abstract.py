from typing import Optional, Union

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
    def get_validated_url(self, value: str) -> Union[str, None]: ...
    def get_validated_price(self, value: str) -> Union[str, None]: ...
    def get_validated_image(self, value: str) -> Union[str, None]: ...

    def result(self, **kwargs) -> Optional[SearchResult]:
        if not kwargs["url"] or not kwargs["price"] or not kwargs["image"]:
            return None
        return SearchResult(**kwargs)
