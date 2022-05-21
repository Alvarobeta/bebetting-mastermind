from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour


@dataclass
class Guessing:
    id: int
    code: List[GuessColour]
    owner_id: int

    def __str__(self) -> str:
        return f"Guessing(id={self.id}, code={self.code}, owner_id={self.owner_id})"
