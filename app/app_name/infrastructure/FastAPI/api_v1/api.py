from fastapi import APIRouter

from app.app_name.infrastructure.FastAPI.api_v1.endpoints import genericendpoint

api_router = APIRouter()
api_router.include_router(genericendpoint.router, tags=["genericendpoint"])
