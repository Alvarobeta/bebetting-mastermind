from dataclasses import dataclass
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour


@dataclass
class Feedback:
    feedback: List[FeedbackColour]
