import logging
import os

from dataclasses import dataclass

from app.mastermind.application.make_a_guess.make_a_guess_command import \
    MakeAGuessCommand
from app.mastermind.application.game_db_actions import game_db_actions

from app.mastermind.domain.entities.guess_colour import GuessColour
# from app.mastermind.domain.entities.guessing_pattern import GuessingPattern
from app.mastermind.domain.entities.response_feedback import ResponseFeedback
from app.mastermind.domain.feedback_provider_service import \
    FeedbackProviderService
from app.mastermind.domain.game_events_service import GameEventsService

from app.mastermind.infrastructure.FastAPI.api_v1.wrong_guess_input_exception import \
    WrongInputException
# from models import Guessing
from schema import Guessing as SchemaGuessing


logger = logging.getLogger(__name__)


@dataclass
class MakeAGuessHandler:
    def __call__(self, command: MakeAGuessCommand) -> ResponseFeedback:
        feedback_provider = FeedbackProviderService()
        game_events = GameEventsService()

        if len(command.pattern.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(
            GuessColour.EMPTY == c for c in command.pattern.code
        ):
            raise WrongInputException()

        # get game
        game = game_db_actions.get_game(game_id=command.game_id)
        
        #update attempts
        game.attempts = 1 if game.attempts == None else game.attempts + 1

        logger.debug(
            f" -------------- game={game}, game code={game.code}"
        )

        guessing = SchemaGuessing(
            code=command.pattern.code,
            owner_id=game.id        
        )

        #add new guessing
        game_guessing = game_db_actions.create_game_guessing(guessing=guessing)

        logger.debug(
            f" -------------- game_guessing={game_guessing}, game_guessing code={game_guessing.code}"
        )
        
        #update game
        game_db_actions.update_game(game=game)

        feedback = feedback_provider.get_feedback(
            codemaker_pattern_raw=game.code, guess_attempt_pattern=command.pattern
        )

        response = ResponseFeedback(feedback=feedback, message="Keep trying!", attempts=game.attempts)

        # check win scenario
        if game_events.won_game(feedback=feedback):
            return ResponseFeedback(feedback=feedback, message="YOU WON!!!!!!!!!", attempts=game.attempts)

        # check lose scenario if attempts = max
        if game.attempts == int(os.environ["DEFAULT_MAX_ATTEMPTS"]):
            return ResponseFeedback(feedback=feedback, message="YOU LOST!!!!!!!!!", attempts=game.attempts)

        # not win -> increment attempt and save history into game
        return response
