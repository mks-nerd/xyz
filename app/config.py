import os
from functools import lru_cache
from logging import getLogger

from pydantic import AnyUrl
from pydantic_settings import BaseSettings

log = getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    # database_url: AnyUrl = None


def get_db_url() -> str:
    if os.getenv("TESTING") is None:
        return os.getenv("DATABASE_TEST_URL", "")
    return os.getenv("DATABASE_URL", "")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
