from typing import List

from fastapi import APIRouter

from app.mastermind.application.list_game_history.list_game_history_usecase import \
    ListGameHistoryUseCase
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.sql_alchemy.game_repository_sql_alchemy import \
    GameRepositorySqlAlchemy

router = APIRouter()


@router.get("/game/{game_id}/historical", response_model=List[GuessColour])
async def get_historical(game_id: int):
    list_game_history = ListGameHistoryUseCase(
        gameRepository=GameRepositorySqlAlchemy()
    )

    return list_game_history(game_id=str(game_id))
