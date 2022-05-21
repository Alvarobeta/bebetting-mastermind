import os

from dataclasses import dataclass
from typing import List, ClassVar

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.entities.guessing import Guessing


@dataclass
class Game:
    id: int
    code: List[GuessColour]
    attempts: int
    guessings: List[Guessing]

    # MAX_ATTEMPTS: ClassVar[int] = int(os.environ["DEFAULT_MAX_ATTEMPTS"])
    # CODE_LENGTH: ClassVar[int] = int(os.environ["DEFAULT_CODE_LENGTH"])

    def __str__(self) -> str:
        return f"Game(id={self.id}, code={self.code}, attempts={self.attempts}, guessings={self.guessings})"
