from fastapi import APIRouter

from models import Game as ModelGame
from fastapi_sqlalchemy import db

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/game/{game_id}")
async def get_game( game_id: int):
    logger.debug(f"--------------------- game_id={game_id}")
    return db.session.query(ModelGame).filter(ModelGame.id == game_id).first()
