from typing import List

from decouple import Csv, config
from loguru import logger

PROJECT_NAME = "fakerz"

PROJECT_DESCRIPTION = "Fake API server"

PROJECT_VERSION = "0.1.0"

DOCS_URL = "/docs"

REDOC_URL = "/redoc"

OPENAPI_URL = "/openapi.json"

ALLOWED_HOSTS: List = config(
    "ALLOWED_HOSTS", cast=Csv(str), default="127.0.0.1, localhost"
)

DEBUG = config("DEBUG", cast=bool, default=True)

CORS_ORIGINS = ["*"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["*"]
CORS_ALLOW_HEADERS = ["*"]

logger.add(
    "output_{time:YYYY-MM-DD at HH:mm:ss}.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    backtrace=False,
    diagnose=False,
    rotation="12:00",
)
