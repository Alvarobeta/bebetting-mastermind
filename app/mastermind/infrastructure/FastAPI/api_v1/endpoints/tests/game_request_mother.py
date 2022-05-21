import os
import random
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour


class GameRequestMother:
    def __init__(self, code: List[GuessColour] = None):
        self._code = code or self._generate_code()

    @staticmethod
    def _generate_code() -> List[str]:
        code = []

        for i in range(int(os.environ["DEFAULT_CODE_LENGTH"])):
            code.append(random.choice(list(GuessColour)))

        return code

    def build(self) -> dict:
        return {"code": self._code}
