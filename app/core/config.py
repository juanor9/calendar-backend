# app/core/config.py
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",  # <-- permite variables adicionales como env, port, etc.
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
