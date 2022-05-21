import logging

from fastapi import APIRouter

from app.mastermind.application.game_db_actions import game_db_actions
from schema import Game as SchemaGame

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    return game_db_actions.create_game(game=game)
