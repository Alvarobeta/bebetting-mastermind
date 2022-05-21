from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour


class WinCondition:
    def check_win_condition(self, feedback: List[FeedbackColour]) -> bool:

        return all(f == FeedbackColour.BLACK for f in feedback)
