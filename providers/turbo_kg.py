import httpx
import parsel

from schemas.search import Query
from .abstract import AbstractProvider


class TurboKGProvider(AbstractProvider):
    async def job(self, query: Query):
        search_url = f"{self.url}/?maker={query.brand.lower()}&model={query.model.lower()}"
        async with httpx.AsyncClient() as client:
            response = await client.get(search_url)
            html = parsel.Selector(text=response.text)
            image_selector_pattern = '.card > .card-img-top > .swiper-container > .swiper-wrapper > div:nth-child(2) > a > img'
            price_selector_pattern = "div > a > p > b.float-right::text"

            return list(map(lambda x: self.result(
                url=f"{self.url}{x.css('div > a').xpath('@href').get()}",
                price=x.css(price_selector_pattern).get(),
                image=x.css(
                    image_selector_pattern
                ).xpath('@data-srcset').get().split(" ")[0] if x.css(
                    image_selector_pattern) else None
            ), html.css("#cars > .car")))
