import logging
import os

from fastapi import APIRouter
from fastapi_sqlalchemy import db

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.FastAPI.api_v1.wrong_guess_input_exception import \
    WrongInputException
from models import Game as ModelGame
from schema import Game as SchemaGame

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    if len(game.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(
        GuessColour.EMPTY == c for c in game.code
    ):
        raise WrongInputException()

    db_game = ModelGame(code=game.code, attempts=0)

    db.session.add(db_game)
    db.session.commit()
    return db_game
