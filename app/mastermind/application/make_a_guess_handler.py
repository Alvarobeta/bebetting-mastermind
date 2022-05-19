

from dataclasses import dataclass
from typing import List

from app.mastermind.application.make_a_guess_command import MakeAGuessCommand
from app.mastermind.domain.feedback_provider_service import FeedbackProviderService

import logging

logger = logging.getLogger(__name__)

@dataclass
class MakeAGuessHandler:
    def __call__(self, command: MakeAGuessCommand) -> List[str]:
        feedback_provider = FeedbackProviderService()
            
        logger.debug(
            f" -------------------------------------  command={command}"
        )

        return feedback_provider.get_feedback(command.game_id, command.pattern)