import uvicorn


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fakerz.settings import settings
from profiles import views as profiles_views

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=settings.OPENAPI_URL,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

app.include_router(profiles_views.router, prefix="/profiles")

if __name__ == "__main__" and settings.DEBUG:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
