import sys
from typing import List

from pydantic import BaseSettings
from loguru import logger


class Settings(BaseSettings):

    PROJECT_NAME: str = "fakerz"

    PROJECT_DESCRIPTION: str = "Fake API server"

    PROJECT_VERSION: str = "0.1.0"

    DOCS_URL: str = "/docs"

    REDOC_URL: str = "/redoc"

    OPENAPI_URL: str = "/openapi.json"

    ALLOWED_HOSTS: List[str] = ["127.0.0.1", "localhost"]

    DEBUG: bool

    SECRET_KEY: str

    CORS_ORIGINS: List[str] = ["*"]

    CORS_ALLOW_CREDENTIALS: bool = True

    CORS_ALLOW_METHODS: List[str] = ["*"]

    CORS_ALLOW_HEADERS: List[str] = ["*"]

    # Don't decrease this number unless you have a good reason not to.
    # Please read
    # https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#maximum-password-lengths
    MINIMUM_PASSWORD_LENGTH: int = 8

    # Don't increase this number unless you have a good reason not to.
    # Please read
    # https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#maximum-password-lengths
    MAXIMUM_PASSWORD_LENGTH: int = 16

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()

logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
