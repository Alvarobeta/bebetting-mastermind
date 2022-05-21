from fastapi import APIRouter

from app.mastermind.application.game_db_actions import game_db_actions

router = APIRouter()


@router.get("/game/{game_id}")
async def get_game(game_id: int):
    return game_db_actions.get_game(game_id=game_id)
