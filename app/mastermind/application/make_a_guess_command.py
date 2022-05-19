

from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.guessing_pattern import GuessingPattern

@dataclass
class MakeAGuessCommand:
    game_id: int
    pattern: GuessingPattern