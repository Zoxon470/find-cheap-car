from httpx import AsyncClient

from pydantic import AnyHttpUrl


class AbstractProvider:
    def __init__(self, http_client: AsyncClient, name: str, url: AnyHttpUrl):
        self.http_client = http_client
        self.name = name
        self.url = url

    async def job(self, query: str): ...

    async def result(self, *args, **kwargs):
        pass
