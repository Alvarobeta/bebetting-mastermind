import requests

from typing import List

from app.mastermind.domain.entities.guessing_pattern import GuessingPattern
from app.mastermind.domain.entities.response_feedback import ResponseFeedback

from models import Game as ModelGame
from fastapi_sqlalchemy import db

import logging
logger = logging.getLogger(__name__)

class FeedbackProviderService:
    # def __init__(self, guess_attempt_pattern: List[str]):
    #     self.guess_attempt_pattern = guess_attempt_pattern

    def get_feedback(
        self, game_id: int, guess_attempt_pattern: GuessingPattern
    ) -> List[str]:

        logger.debug(
            f" -------------------------------------  game_id={game_id}, guess_attempt_pattern={guess_attempt_pattern}"
        )

        #get game
        r = db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

        
        logger.debug(
            f" -------------------------------------  response gameId={r.id}, game code={r.code}"
        )
        
        # response = ResponseFeedback(
        #     feedback=["BLACK", "WHITE", "WHITE", ""])

        return ["BLACK", "WHITE", "WHITE", ""]