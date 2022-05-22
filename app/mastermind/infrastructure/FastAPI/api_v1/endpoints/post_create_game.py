import logging
from dataclasses import dataclass
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.mastermind.application.create_game.create_game_dto import \
    CreateGameDto
from app.mastermind.application.create_game.create_game_usecase import \
    CreateGameUsecase
from app.mastermind.application.exceptions.wrong_input_exception import \
    WrongInputException
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.sql_alchemy.game_repository_sql_alchemy import \
    GameRepositorySqlAlchemy

logger = logging.getLogger(__name__)

router = APIRouter()


class Code(BaseModel):
    code: List[GuessColour]


@dataclass
class Response:
    id: str


@router.post("/games", response_model=Response)
async def create_game(new_game_code: Code) -> Response:
    if len(new_game_code.code) != Game.CODE_LENGTH or any(
        GuessColour.EMPTY == c for c in new_game_code.code
    ):
        raise WrongInputException(message=f"You must input {Game.CODE_LENGTH} colours.")

    create_game = CreateGameUsecase(gameRepository=GameRepositorySqlAlchemy())
    game = create_game(CreateGameDto(code=new_game_code.code))

    return Response(id=str(game.id))
