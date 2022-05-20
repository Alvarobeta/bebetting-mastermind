from enum import Enum


class GuessColour(str, Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    ORANGE = "ORANGE"
    BLUE = "BLUE"
    PINK = "PINK"
    GREEN = "GREEN"
    EMPTY = ""

    def __str__(self) -> str:
        return self.value
