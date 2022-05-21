from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour


@dataclass
class Game:
    id: int
    code: List[GuessColour]
    attempts: int
    # guessing_history

    # MAX_ATTEMPTS: ClassVar[int] = int(os.enviro)

    def __str__(self) -> str:
        return f"Game(id={self.id}, code={self.code}, attempts={self.attempts})"
