from .mashina_kg import MashinaKGProvider
from .turbo_kg import TurboKGProvider

mashina_kg = MashinaKGProvider(
    name="MashinaKG",
    url="https://www.mashina.kg"
)
turbo_kg = TurboKGProvider(
    name="TurboKG",
    url="https://turbo.kg"
)

providers = [
    mashina_kg,
    turbo_kg,
]
