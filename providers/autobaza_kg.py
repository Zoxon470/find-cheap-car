from typing import Union

import httpx
import parsel

from core.utils import get_converted_currency
from schemas.search import Query
from .abstract import AbstractProvider


class AutobazaKGProvider(AbstractProvider):
    def get_validated_price(self, value: str) -> Union[str, None]:
        if value:
            return value.replace(" ", "")[1:-3]
        return None

    async def job(self, query: Query):
        search_url = f"{self.url}/cars/bmw/6-seriya"
        async with httpx.AsyncClient() as client:
            response = await client.get(search_url)
            html = parsel.Selector(text=response.text)

            price_selector_pattern = ".b-list-card__inner > h4 > a > span:nth-child(2)::text"
            cars = []
            for car in html.css(".row > .col-md-9 > .b-list-card"):
                cars.append(self.result(
                    url=car.css(".b-list-card__media > a").xpath('@href').get(),
                    price=await get_converted_currency(
                        self.get_validated_price(
                            car.css(price_selector_pattern).get()
                        )
                    ),
                    image=car.css(".b-list-card__media > a > img").xpath("@src").get(),
                ))
            return cars
