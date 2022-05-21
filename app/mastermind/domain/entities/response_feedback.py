from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour


@dataclass
class ResponseFeedback:
    feedback: List[FeedbackColour]
    message: str = ""
    attempts: int = 0

    def __str__(self) -> str:
        return f"ResponseFeedback(feedback={self.feedback}, message={self.message}, attempts={self.attempts})"
