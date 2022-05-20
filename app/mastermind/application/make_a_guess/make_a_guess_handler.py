import logging
import os

from dataclasses import dataclass
from typing import List
from app.mastermind.domain.entities.response_feedback import ResponseFeedback
from fastapi_sqlalchemy import db
from models import Game as ModelGame

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.game_events_service import GameEventsService
from app.mastermind.infrastructure.FastAPI.api_v1.wrong_guess_input_exception import WrongInputException
from app.mastermind.application.make_a_guess.make_a_guess_command import \
    MakeAGuessCommand
from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.feedback_provider_service import \
    FeedbackProviderService


logger = logging.getLogger(__name__)



@dataclass
class MakeAGuessHandler:
    def __call__(self, command: MakeAGuessCommand) -> ResponseFeedback:
        feedback_provider = FeedbackProviderService()
        game_events = GameEventsService()

        if len(command.pattern.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(GuessColour.EMPTY == c for c in command.pattern.code):
            raise WrongInputException()
            
        logger.debug(f" --------------  command={command}")

        # #get game TODO call the API??
        game = db.session.query(ModelGame).filter(ModelGame.id == command.game_id).first()

        game.attempts = 1 if game.attempts == None else game.attemtps + 1

        logger.debug(f" --------------  game code={game.code}, game attempts={game.attempts}")
        feedback = feedback_provider.get_feedback(
            codemaker_pattern_raw=game.code, guess_attempt_pattern=command.pattern
        ) 
        response = ResponseFeedback(feedback=feedback, msg="Keep trying!")

        #check win scenario
        if game_events.won_game(feedback=feedback):
            return ResponseFeedback(feedback=feedback, msg="YOU WON!!!!!!!!!")

        #check lose scenario if attempts = max
        if game.attempts == int(os.environ["DEFAULT_MAX_ATTEMPTS"]):
            return ResponseFeedback(feedback=feedback, msg="YOU LOSE!!!!!!!!!")

        #not win -> increment attempt and save history into game
        return response
