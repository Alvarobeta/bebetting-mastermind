import logging

import uuid
from enum import Enum
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.guess_colour import GuessColour
# from app.mastermind.application.exceptions.wrong_game_status_exception import WrongGameStatusException
from app.mastermind.application.exceptions.wrong_game_status_exception import WrongGameStatusException

logger = logging.getLogger(__name__)

class GAME_STATUS(str, Enum):
    PLAYING = "Playing"
    WON = "Won"
    LOST = "Lost"


class Game:
    id: str
    code: List[GuessColour]
    attempts: List[List[GuessColour]]
    status: GAME_STATUS
    feedbacks: List[List[FeedbackColour]]

    CODE_LENGTH: int = 4
    GAME_LIMIT: int = 8

    # MAX_ATTEMPTS: ClassVar[int] = int(os.environ["DEFAULT_MAX_ATTEMPTS"])
    # CODE_LENGTH: ClassVar[int] = int(os.environ["DEFAULT_CODE_LENGTH"])

    def __init__(self, code) -> None:
        self.id = str(uuid.uuid4())
        self.code = code
        self.attempts = []
        self.feedbacks = []
        self.status = GAME_STATUS.PLAYING

    def __str__(self) -> str:
        return f"Game(id={self.id}, code={self.code}, attempts={self.attempts}, feedbacks={self.feedbacks}, status={self.status})"

    def make_guess(self, guess: List[GuessColour]):
        if (self.status != GAME_STATUS.PLAYING):
            raise WrongGameStatusException(message=F'You cannot play. Status is {self.status}') 

        logger.debug(f" -------------- guess={guess} --------------")
        self.attempts.append(guess)

        logger.debug(f" -------------- self={self} --------------")
        logger.debug(f" -------------- attempts={self.attempts} --------------")

        # compute last feedback
        feedback = self.compute_last_feedback(guess)

        logger.debug(f" -------------- feedback={feedback} --------------")

        self.feedbacks.append(feedback)

        logger.debug(f" -------------- feedbacks={self.feedbacks} --------------")

        # # if last feedback is all black TODO
        # self.status = GAME_STATUS.WON

        # # if last feedback
        # # or is this the last move?
        # self.status = GAME_STATUS.LOST

    def compute_last_feedback(self, guess: List[GuessColour]) -> List[FeedbackColour]:
        feedback: List[FeedbackColour] = []

        for index, colour in enumerate(guess):
            if any(colour == c for c in self.code):
                if guess[index] == self.code[index]:
                    feedback.append(FeedbackColour.BLACK)

                else:
                    feedback.append(FeedbackColour.WHITE)

                self.code[
                    index
                ] = GuessColour.EMPTY  # avoid erroneous comparisons on repeated colors

            else:
                feedback.append(FeedbackColour.EMPTY)
        
        return feedback
