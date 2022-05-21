from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.entities.guessing import Guessing


@dataclass
class Game:
    id: int
    code: List[GuessColour]
    attempts: int
    guessings: List[Guessing]

    # MAX_ATTEMPTS: ClassVar[int] = int(os.enviro)

    def __str__(self) -> str:
        return f"Game(id={self.id}, code={self.code}, attempts={self.attempts}, guessings={self.guessings})"
