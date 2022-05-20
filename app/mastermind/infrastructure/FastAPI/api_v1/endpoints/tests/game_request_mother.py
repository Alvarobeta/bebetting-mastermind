import random

from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour

class GameRequestMother:
    def __init__(self, code: List[GuessColour] = None):
        self._code = code or self._generate_code()

    @staticmethod
    def _generate_code() -> List[str]:
        code = []
        default_code_length = 4

        for i in range(default_code_length):
            code.append(random.choice(list(GuessColour)))
        
        return code

    def build(self) -> dict:
        return {"code": self._code}
