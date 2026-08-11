from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.core.config import settings
from app.api.users import router as users_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)


app.include_router(
    health_router,
    prefix=settings.api_prefix,
)

app.include_router(
    auth_router,
    prefix=settings.api_prefix,
)

app.include_router(
    users_router,
    prefix=settings.api_prefix,
)

@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "documentation": "/docs",
        "health": f"{settings.api_prefix}/health",
    }
