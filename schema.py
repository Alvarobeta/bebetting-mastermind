from typing import List
from app.mastermind.domain.entities.game import GAME_STATUS
from pydantic import BaseModel


class Game(BaseModel):
    code: List[str]
    attempts: List[List[str]]
    status: GAME_STATUS
    feedbacks: List[List[str]]

    class Config:
        orm_mode = True
