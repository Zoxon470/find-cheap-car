from typing import Union

import aioredis
import httpx
import orjson

from core.config import settings


async def get_converted_currency(
        amount: str,
        from_currency: str = "KGS",
        to_currency: str = "USD",
) -> Union[int, None]:
    if not amount:
        return None

    if from_currency in ("KGS", "USD"):
        redis = await aioredis.from_url(f"redis://{settings.REDIS_HOST}/0")
        currencies_rate_from_cache = await redis.get(from_currency)
        if not currencies_rate_from_cache:
            async with httpx.AsyncClient() as client:
                response_currencies_rate = await client.get(
                    f"https://open.er-api.com/v6/latest/{from_currency}"
                )
                await redis.set(
                    from_currency,
                    orjson.dumps(response_currencies_rate.json()["rates"]),
                    ex=300
                )
                currencies_rate_from_cache = await redis.get(from_currency)
                currencies_rate = orjson.loads(currencies_rate_from_cache)
                return round(
                    int(amount) / currencies_rate[from_currency]
                    * currencies_rate[to_currency]
                )
        else:
            currencies_rate = orjson.loads(currencies_rate_from_cache)
            return round(
                int(amount) / currencies_rate[from_currency]
                * currencies_rate[to_currency]
            )
    else:
        return None
