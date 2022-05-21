# from sqlalchemy.orm import Session

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.infrastructure.FastAPI.api_v1.wrong_guess_input_exception import WrongInputException
from fastapi_sqlalchemy import db

from models import Game as ModelGame, Guessing
from models import Guessing as ModelGuessing
from schema import Game as SchemaGame
from schema import Guessing as SchemaGuessing

import os

import logging
logger = logging.getLogger(__name__)


def get_game(game_id: int):
    return db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

def create_game(game: SchemaGame):
    if len(game.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(
        GuessColour.EMPTY == c for c in game.code
    ):
        raise WrongInputException()

    db_game = ModelGame(
        code=game.code, 
        attempts=0,)

    db.session.add(db_game)
    db.session.commit()

    return db_game

def update_game(game: SchemaGame):
    db.session.add(game)
    db.session.commit()
    db.session.refresh(game)

def create_game_guessing(guessing: SchemaGuessing):
    db_guessing = ModelGuessing(**guessing.dict())
    db.session.add(db_guessing)
    db.session.commit()
    db.session.refresh(db_guessing)

    return db_guessing