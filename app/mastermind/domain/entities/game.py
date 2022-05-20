
from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour


@dataclass
class Game:
    id: int
    code: List[GuessColour]
    #attempts
    #guessing_history
    