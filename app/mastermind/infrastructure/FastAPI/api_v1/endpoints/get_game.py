import code
from fastapi import APIRouter
# from models import User as ModelUser
# from schema import User as SchemaUser
from models import Game as ModelGame
from schema import Game as SchemaGame
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

import logging

router = APIRouter()

logger = logging.getLogger(__name__)

@router.get("/game/{game_id}")
async def get_game( game_id: int):
    logger.debug(f"--------------------- game_id={game_id}")
    return db.session.query(ModelGame).filter(ModelGame.id == game_id).first()
