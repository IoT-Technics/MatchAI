from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MatchAI API"
    app_version: str = "0.1.0"

    api_prefix: str = "/api/v1"

    debug: bool = True

    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str = (
        "postgresql+psycopg://matchai:matchai@localhost:5432/matchai"
    )

    jwt_secret_key: str = "CHANGE-ME-IN-ENV"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()