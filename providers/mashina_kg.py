from typing import Union

import httpx
import parsel

from schemas.search import Query
from .abstract import AbstractProvider


class MashinaKGProvider(AbstractProvider):
    def get_validated_price(self, value: str) -> Union[str, None]:
        if value:
            return value.replace(" ", "")[1:]
        return None

    async def job(self, query: Query):
        search_url = f"{self.url}/search/{query.brand.lower()}/{query.model.lower()}"
        async with httpx.AsyncClient() as client:
            response = await client.get(search_url)
            html = parsel.Selector(text=response.text)

            return list(map(lambda x: self.result(
                url=f"{self.url}{x.xpath('@href').get()}",
                price=self.get_validated_price(
                    x.css("div > p > strong::text").get()
                ),
                image=x.css(
                    ".thumb-item-carousel"
                )[0].css("img")[0].xpath("@data-src").get()
            ), html.css(".table-view-list .list-item > a")))
