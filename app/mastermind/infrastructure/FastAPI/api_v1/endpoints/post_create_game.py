from dataclasses import dataclass
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.mastermind.application.create_game.create_game_usecase import \
    CreateGameUsecase
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.sql_alchemy.game_repository_sql_alchemy import \
    GameRepositorySqlAlchemy

router = APIRouter()


class Code(BaseModel):
    code: List[GuessColour]


@dataclass
class Response:
    id: str


@router.post("/api/games", response_model=Response)
async def create_game() -> Response:
    create_game = CreateGameUsecase(gameRepository=GameRepositorySqlAlchemy())

    game = create_game()

    return Response(id=str(game.id))
