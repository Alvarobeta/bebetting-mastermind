from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour


@dataclass
class Feedback:
    feedback: List[FeedbackColour]

    def __str__(self) -> str:
        return f"Feedback(feedback={self.feedback})"
