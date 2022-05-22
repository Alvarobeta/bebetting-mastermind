import random
from enum import Enum
from typing import List

from app.mastermind.domain.entities.game import Game


class ValidGuessColour(str, Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    BLUE = "BLUE"
    PINK = "PINK"
    GREEN = "GREEN"


class GameRequestMother:
    def __init__(self, code: List[str] = None):
        self._code = code or self._generate_code()

    @staticmethod
    def _generate_code() -> List[str]:
        code = []

        for i in range(Game.CODE_LENGTH):
            code.append(random.choice(list(ValidGuessColour)))

        return code

    def build(self) -> dict:
        return {"code": self._code}
