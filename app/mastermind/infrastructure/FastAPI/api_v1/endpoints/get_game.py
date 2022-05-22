import logging

from fastapi import APIRouter

from app.mastermind.application.get_game.get_game_usecase import GetGameUseCase
from app.mastermind.infrastructure.sql_alchemy.game_repository_sql_alchemy import \
    GameRepositorySqlAlchemy

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/game/{game_id}")
async def get_game(game_id: str):
    game = GetGameUseCase(gameRepository=GameRepositorySqlAlchemy())

    logger.debug(f"---------- game={game} ----------")

    return game(game_id=game_id)
