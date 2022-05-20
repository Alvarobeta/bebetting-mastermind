import os
from app.mastermind.application.make_a_guess.wrong_guess_input_exception import WrongGuessInputException
from fastapi import APIRouter, HTTPException
from models import Game as ModelGame
from schema import Game as SchemaGame
from fastapi_sqlalchemy import db

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    if len(game.code) != int(os.environ["DEFAULT_CODE_LENGTH"]):
        raise WrongGuessInputException()

    db_game = ModelGame(
        code=game.code
    )

    db.session.add(db_game)
    db.session.commit()
    return db_game
