from typing import Union

import httpx
import parsel

from core.utils import get_converted_currency
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

            cars = []
            for car in html.css(".table-view-list .list-item > a"):
                cars.append(self.result(
                    url=f"{self.url}{car.xpath('@href').get()}",
                    price=await get_converted_currency(
                        self.get_validated_price(
                            car.css("div > p > strong::text").get(),
                        ),
                        from_currency="USD",
                        to_currency="KGS"
                    ),
                    image=car.css(
                        ".thumb-item-carousel"
                    )[0].css("img")[0].xpath("@data-src").get()
                ))
            return cars
