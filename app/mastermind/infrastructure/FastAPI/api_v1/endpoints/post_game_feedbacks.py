from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.mastermind.application.make_a_guess.make_a_guess_dto import \
    MakeAGuessDto
from app.mastermind.application.make_a_guess.make_a_guess_usecase import \
    MakeAGuessUsecase
from app.mastermind.domain.entities.guessing_pattern import GuessingPattern
from app.mastermind.infrastructure.sql_alchemy.game_repository_sql_alchemy import \
    GameRepositorySqlAlchemy

router = APIRouter()


class Response(BaseModel):
    message: str = ""
    attempts: int = 0
    feedback: List[str]


@router.post("/api/games/{game_id}/feedbacks", response_model=Response)
async def get_feedback(game_id: str, guess_attempt_pattern: GuessingPattern):
    handler = MakeAGuessUsecase(gameRepository=GameRepositorySqlAlchemy())

    return handler(
        MakeAGuessDto(
            game_id=game_id,
            pattern=guess_attempt_pattern,
        )
    )
