from fastapi import APIRouter

from app.mastermind.infrastructure.FastAPI.api_v1.endpoints import \
    genericendpoint
from app.mastermind.infrastructure.FastAPI.api_v1.endpoints import \
    create_game

api_router = APIRouter()
api_router.include_router(genericendpoint.router, tags=["genericendpoint"])
api_router.include_router(create_game.router, tags=["create game"])
