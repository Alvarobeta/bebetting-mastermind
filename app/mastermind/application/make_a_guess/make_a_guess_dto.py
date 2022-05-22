from dataclasses import dataclass

from app.mastermind.application.exceptions.wrong_input_exception import \
    WrongInputException
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.entities.guessing_pattern import GuessingPattern


@dataclass
class MakeAGuessDto:
    game_id: str
    pattern: GuessingPattern

    def __init__(self, pattern: GuessingPattern, game_id: str) -> None:
        self.pattern = pattern
        self.game_id = game_id

        if len(pattern.code) != Game.CODE_LENGTH:
            raise WrongInputException(message="Invalid guessing length")

        if any(GuessColour.EMPTY == c for c in pattern.code):
            raise WrongInputException(message="Empty colour")
