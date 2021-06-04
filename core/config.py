from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVICE_NAME: str = "Find cheap car"
    DEBUG: bool = True
    DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
