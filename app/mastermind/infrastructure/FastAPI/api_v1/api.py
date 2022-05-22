from fastapi import APIRouter

from app.mastermind.infrastructure.FastAPI.api_v1.endpoints import (
    genericendpoint, get_game, get_game_guessing_historical, post_create_game,
    post_game_feedbacks)

api_router = APIRouter()
api_router.include_router(genericendpoint.router, tags=["genericendpoint"])
api_router.include_router(post_create_game.router, tags=["create game"])
api_router.include_router(get_game.router, tags=["get game"])
api_router.include_router(
    get_game_guessing_historical.router, tags=["get game guessing hisorical"]
)
api_router.include_router(post_game_feedbacks.router, tags=["get feedback"])
