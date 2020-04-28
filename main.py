import uvicorn
from Courses import views as courses_views
from fakerz.settings import settings
from fastapi import FastAPI
from profiles import views as profiles_views
from inbox import views as inbox_views
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

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

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": settings.DB_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(profiles_views.router, prefix="/profiles")
app.include_router(courses_views.router, prefix="/courses")
app.include_router(inbox_views.router, prefix="/inbox")

if __name__ == "__main__" and settings.DEBUG:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
