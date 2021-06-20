from typing import Union

import httpx
import parsel

from core.utils import get_converted_currency
from schemas.search import Query
from .abstract import AbstractProvider


class TurboKGProvider(AbstractProvider):
    def get_validated_price(self, value: str) -> Union[str, None]:
        if value:
            return value.replace(" ", "")[1:-3]
        return None

    async def job(self, query: Query):
        search_url = f"{self.url}/?maker={query.brand.lower()}&model={query.model.lower()}&currency=KGS"
        async with httpx.AsyncClient() as client:
            response = await client.get(search_url)
            html = parsel.Selector(text=response.text)
            image_selector_pattern = '.card > .card-img-top > .swiper-container > .swiper-wrapper > div:nth-child(2) > a > img'
            price_selector_pattern = "div > a > p > b.float-right::text"

            cars = []
            for car in html.css("#cars > .car"):
                cars.append(self.result(
                    url=f"{self.url}{car.css('div > a').xpath('@href').get()}",
                    price=await get_converted_currency(
                        self.get_validated_price(
                            car.css(price_selector_pattern).get()
                        )
                    ),
                    image=car.css(
                        image_selector_pattern
                    ).xpath('@data-srcset').get().split(" ")[0] if car.css(
                        image_selector_pattern) else None
                ))
            return cars
