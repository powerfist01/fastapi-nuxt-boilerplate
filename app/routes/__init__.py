from fastapi import APIRouter

from app.routes import home

api_router = APIRouter(
    prefix="/api",
)

api_router.include_router(home.router)
