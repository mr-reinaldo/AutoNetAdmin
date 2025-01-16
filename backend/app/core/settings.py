from pydantic_settings import BaseSettings, SettingsConfigDict
from decouple import config as env_config
from functools import lru_cache

env_config.encoding = "utf-8"


class Settings(BaseSettings):

    model_config: SettingsConfigDict = {
        "case_sensitive": True,
        "extra": "ignore",
    }

    # FASTAPI ENVIRONMENT VARIABLES
    SECRET_KEY: str = env_config("SECRET_KEY", cast=str)
    API_PREFIX: str = "/api/v1"
    API_TITLE: str = "NPLMW API"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = (
        "NPLMW (Napalm Web API) is a RESTful API for managing network devices using the Napalm library."
    )

    # DATABASE ENVIRONMENT VARIABLES
    DATABASE_URL_DEV: str = env_config("DATABASE_URL_DEV", cast=str)
    DATABASE_URL_PROD: str = env_config("DATABASE_URL_PROD", cast=str)
    ECHO_SQLALCHEMY: bool = env_config("ECHO_SQLALCHEMY", cast=bool)

    # JWT ENVIRONMENT VARIABLES
    JWT_SECRET_KEY: str = env_config("JWT_SECRET_KEY", cast=str)
    JWT_ALGORITHM: str = env_config("JWT_ALGORITHM", cast=str)
    JWT_EXPIRATION_TIME_MINUTES: int = env_config(
        "JWT_EXPIRATION_TIME_MINUTES", cast=int
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
