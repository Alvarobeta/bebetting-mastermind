from typing import List
from pydantic import BaseModel


class Game(BaseModel):
    code: List[str]
    attempts: int = 0
    # guess_history = List[List[str]]

    class Config:
        orm_mode = True