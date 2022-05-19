import code
from fastapi import APIRouter
# from models import User as ModelUser
# from schema import User as SchemaUser
from models import Game as ModelGame
from schema import Game as SchemaGame
from fastapi_sqlalchemy import db

router = APIRouter()


@router.post("/games", response_model=SchemaGame)
async def create_game(game: SchemaGame):
    db_game = ModelGame(
        code=game.code
    )
    db.session.add(db_game)
    db.session.commit()
    return db_game
