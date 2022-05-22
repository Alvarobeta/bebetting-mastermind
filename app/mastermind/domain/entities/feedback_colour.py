from enum import Enum


class FeedbackColour(str, Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    EMPTY = ""

    def __str__(self) -> str:
        return self.value
