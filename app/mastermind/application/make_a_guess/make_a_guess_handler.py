

from dataclasses import dataclass
from typing import List

from app.mastermind.application.make_a_guess.make_a_guess_command import MakeAGuessCommand
from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.feedback_provider_service import FeedbackProviderService
from models import Game as ModelGame
from fastapi_sqlalchemy import db

import logging

logger = logging.getLogger(__name__)

@dataclass
class MakeAGuessHandler:
    def __call__(self, command: MakeAGuessCommand) -> List[FeedbackColour]:
        feedback_provider = FeedbackProviderService()
            
        logger.debug(
            f" --------------  command={command}"
        )
        
        # #get game TODO call the API??
        game = db.session.query(ModelGame).filter(ModelGame.id == command.game_id).first()
        
        logger.debug(
            f" --------------  game={game}"
        )

        return feedback_provider.get_feedback(
            codemaker_pattern_raw=game.code, 
            guess_attempt_pattern=command.pattern
            )