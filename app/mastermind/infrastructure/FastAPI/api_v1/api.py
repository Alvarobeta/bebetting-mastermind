from fastapi import APIRouter

from app.mastermind.infrastructure.FastAPI.api_v1.endpoints import \
    feedback, genericendpoint, create_game, get_game

api_router = APIRouter()
api_router.include_router(genericendpoint.router, tags=["genericendpoint"])
api_router.include_router(create_game.router, tags=["create game"])
api_router.include_router(get_game.router, tags=["get game"])
api_router.include_router(feedback.router, tags=["get feedback"])
