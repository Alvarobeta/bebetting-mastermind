import code
from fastapi import APIRouter
# from models import User as ModelUser
# from schema import User as SchemaUser
from models import Game as ModelGame
from schema import Game as SchemaGame
from fastapi_sqlalchemy import db

import logging

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    
    # logger.debug(
    #     f" ------------------------------------- create_game. game={game}"
    # )

    db_game = ModelGame(
        code=game.code
    )
    db.session.add(db_game)
    db.session.commit()
    return db_game
