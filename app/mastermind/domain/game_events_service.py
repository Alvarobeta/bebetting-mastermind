import logging
from typing import List

from app.mastermind.domain.entities.feedback_colour import FeedbackColour

from app.mastermind.domain.game_services.win_condition import WinCondition

logger = logging.getLogger(__name__)


class GameEventsService:
    def __init__(self):
        self._win_condiction = WinCondition()

    def won_game(
        self, 
        feedback: List[FeedbackColour]
    ) -> bool:

        return self._win_condiction.check_win_condition(feedback=feedback)
        