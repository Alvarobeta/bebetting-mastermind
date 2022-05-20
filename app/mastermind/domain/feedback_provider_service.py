import requests

from typing import List
from app.mastermind.domain.app_service_name.compare_patterns import ComparePatterns

from app.mastermind.domain.entities.guessing_pattern import GuessingPattern
from app.mastermind.domain.entities.response_feedback import ResponseFeedback

from models import Game as ModelGame
from fastapi_sqlalchemy import db

import logging
logger = logging.getLogger(__name__)

class FeedbackProviderService:
    def __init__(self):
        self._compare_patterns = ComparePatterns()

    def get_feedback(
        self, 
        game_id: int, 
        guess_attempt_pattern: GuessingPattern
    ) -> List[str]:

        logger.debug(
            f" ------------------------------------- guess_attempt_pattern={guess_attempt_pattern}"
        )

        #get game
        game = db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

        logger.debug(
            f" -------------------------------------  game_id={game_id}, gamemaker_pattern={game.code}"
        )

        #iterate X times after finish the game and loose TODO
        #compare codebreaker guess pattern with codemaker pattern
        
        feedback: List[str] = self._compare_patterns.compare(
            codebreaker_guess_pattern=guess_attempt_pattern.code,
            codemaker_pattern=game.code)

        logger.debug(
            f" -------------------------------------  feedback={feedback}"
        )
        #compare if the color exist and are in the correct position
        
        # response = ResponseFeedback(
        #     feedback=["BLACK", "WHITE", "WHITE", ""])

        #-------------------------------------------------------
        # def print_mastermind_board(passcode, guess_codes, guess_flags):
 
        # print("-----------------------------------------")
        # print("\t      MASTERMIND")
        # print("-----------------------------------------")
    
        # print("    |", end="")
        # for x in game.code:
        #     print("\t" + x[:3], end="")
        # print() 
    
        # for i in reversed(range(len(guess_attempt_pattern))):
        #     print("-----------------------------------------")
        #     print(guess_flags[i][0], guess_flags[i][1], "|")
            
    
        #     print(guess_flags[i][2], guess_flags[i][3], end=" |")
        #     for x in guess_attempt_pattern[i]:
        #         print("\t" + x[:3], end="")
    
        #     print() 
        # print("-----------------------------------------")
        #-------------------------------------------------------

        return feedback