import logging
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.entities.guessing_pattern import GuessingPattern
from app.mastermind.domain.feedback_services.compare_patterns import \
    ComparePatterns

logger = logging.getLogger(__name__)


class FeedbackProviderService:
    def __init__(self):
        self._compare_patterns = ComparePatterns()

    def get_feedback(
        self, codemaker_pattern_raw: List[str], guess_attempt_pattern: GuessingPattern
    ) -> List[FeedbackColour]:

        codemaker_pattern: List[GuessColour] = [
            GuessColour(c) for c in codemaker_pattern_raw
        ]

        logger.debug(
            f" -------------- guess_attempt_pattern={guess_attempt_pattern}, \
                codemaker_pattern={codemaker_pattern}"
        )

        # iterate X times after finish the game and loose TODO
        feedback: List[FeedbackColour] = self._compare_patterns.compare(
            codebreaker_guess_pattern=guess_attempt_pattern.code,
            codemaker_pattern=codemaker_pattern,
        )

        logger.debug(f" --------------  feedback={feedback}")

        return feedback
