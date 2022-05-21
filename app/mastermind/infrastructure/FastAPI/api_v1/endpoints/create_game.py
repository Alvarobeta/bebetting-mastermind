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


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    return game_db_actions.create_game(game=game)