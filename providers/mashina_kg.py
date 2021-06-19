import httpx
import parsel

from .abstract import AbstractProvider
from schemas.search import Query


class MashinaKGProvider(AbstractProvider):
    async def job(self, query: Query):
        search_url = f"{self.url}/search/{query.brand.lower()}/{query.model.lower()}"
        async with httpx.AsyncClient() as client:
            response = await client.get(search_url)
            html = parsel.Selector(text=response.text)

            return list(map(lambda x: self.result(
                url=f"{self.url}{x.xpath('@href').get()}",
                price=x.css("div > p > strong::text").get(),
                image=x.css(".thumb-item-carousel")[0].css("img")[0].xpath("@data-src").get()
            ), html.css(".table-view-list .list-item > a")))
