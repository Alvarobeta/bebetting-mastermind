from typing import List
from pydantic import BaseModel


# class Guessing(BaseModel):
#     id: int
#     code: List[str]
#     owner_id: int

#     class Config:
#         orm_mode = True

class Game(BaseModel):
    # id: int
    code: List[str]
    attempts: int = 0
    # guessings: List[Guessing] = []

    class Config:
        orm_mode = True
