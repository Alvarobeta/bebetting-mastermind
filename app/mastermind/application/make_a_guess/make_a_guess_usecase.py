import logging
import os
from dataclasses import dataclass
from typing import List
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.entities.guess_colour import GuessColour
# from models import Game as ModelGame

from pydantic import BaseModel

from app.mastermind.application.game_db_actions_TBD import game_db_actions
from app.mastermind.application.make_a_guess.make_a_guess_dto import \
    MakeAGuessDto
from app.mastermind.domain.entities.feedback_colour import FeedbackColour
from app.mastermind.domain.game_repository import GameRepository

logger = logging.getLogger(__name__)


class Response(BaseModel):
    message: str = ""
    attempts: List[List[GuessColour]]
    feedback: List[FeedbackColour]


@dataclass
class MakeAGuessUsecase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, command: MakeAGuessDto) -> Response:

        # get game
        # game = game_db_actions.get_game(game_id=command.game_id)
        db_game = self.gameRepository.get_by_id(game_id=command.game_id)
        game = Game(code=db_game.code)

        logger.debug(f" -------------- game={game}")

        # update attempts
        # game.attempts = 1 if game.attempts == None else game.attempts + 1

        game.make_guess(command.pattern.code)

        self.gameRepository.save(game)

        #{status: game.status, feedback: game.feedbacks.pop()}

        logger.debug(f" -------------- game after saved={game}")
        logger.debug(f" -------------- game after saved attempts={game.attempts}")

        return Response(message="Keep trying!", feedback=game.feedbacks.pop(), attempts=game.attempts)

        if game.status == won:
            return asdic
        elif game.status == lose:
            return asdadf
        elif game.status == playing:
            return ResponseFeedback(
                feedback=feedback, message="Keep trying!", attempts=game.attempts
            )
        else:
            raise RuntimeError(asd)

        # logger.debug(f" -------------- game={game}, game code={game.code}")

        guessing = SchemaGuessing(code=command.pattern.code, owner_id=game.id)

        # add new guessing
        game_guessing = game_db_actions.create_game_guessing(guessing=guessing)

        # logger.debug(
        #     f" -------------- game_guessing={game_guessing}, game_guessing code={game_guessing.code}"
        # )

        # update game
        game_db_actions.update_game(game=game)

        feedback = feedback_provider.get_feedback(
            codemaker_pattern_raw=game.code, guess_attempt_pattern=command.pattern
        )

        response = ResponseFeedback(
            feedback=feedback, message="Keep trying!", attempts=game.attempts
        )

        # check win scenario
        if game_events.won_game(feedback=feedback):
            return ResponseFeedback(
                feedback=feedback, message="YOU WON!!!!!!!!!", attempts=game.attempts
            )

        # check lose scenario if attempts = max
        if game.attempts == int(os.environ["DEFAULT_MAX_ATTEMPTS"]):
            return ResponseFeedback(
                feedback=feedback, message="YOU LOST!!!!!!!!!", attempts=game.attempts
            )

        # not win -> increment attempt and save history into game
        return response
