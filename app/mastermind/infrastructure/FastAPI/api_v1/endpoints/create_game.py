import logging
import os

from fastapi import APIRouter
from fastapi_sqlalchemy import db

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.FastAPI.api_v1.wrong_guess_input_exception import \
    WrongInputException
from app.mastermind.application.game_db_actions import game_db_actions

from models import Game as ModelGame
from schema import Game as SchemaGame

logger = logging.getLogger(__name__)

router = APIRouter()


# @router.post("/games", response_model=SchemaGame)
# async def create_game(game: SchemaGame):
#     if len(game.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(GuessColour.EMPTY == c for c in game.code):
#         raise WrongInputException()

#     logger.debug(f" --------------  game={game}")
#     db_game = ModelGame(
#         code=game.code, 
#         attempts=0,)

#     logger.debug(f" --------------  db_game={db_game}")

#     db.session.add(db_game)
#     db.session.commit()
#     # db.session.refresh(db_game)
#     return db_game

@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    return game_db_actions.create_game(game=game)