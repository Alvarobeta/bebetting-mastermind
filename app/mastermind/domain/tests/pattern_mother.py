import random
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour


class PatternMother:
    @staticmethod
    def build(
        pattern: List[GuessColour] = [
            random.choice(list(GuessColour)),
            random.choice(list(GuessColour)),
            random.choice(list(GuessColour)),
            random.choice(list(GuessColour)),
        ]
    ):

        return pattern
