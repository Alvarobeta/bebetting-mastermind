import json

from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from app.mastermind.application.exceptions.end_game_exception import \
    EndGameException
from app.mastermind.application.make_a_guess.make_a_guess_dto import \
    MakeAGuessDto
from app.mastermind.domain.entities.game import GAME_STATUS, Game
from app.mastermind.domain.game_repository import GameRepository


class Response(BaseModel):
    message: str = ""
    attempts: int = 0
    feedback: List[str]


@dataclass
class MakeAGuessUsecase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, command: MakeAGuessDto) -> Response:
        db_game = self.gameRepository.get_by_id(game_id=command.game_id)

        game = Game(
            id=db_game.id,
            code=db_game.code,
            attempts=db_game.attempts,
            feedbacks=db_game.feedbacks,
            status=db_game.status,
        )

        game.make_guess(command.pattern.code)

        self.gameRepository.save(game)

        if game.status == GAME_STATUS.WON:
            raise EndGameException(
                type="GAME_WON_STATUS", message="Congratulations, you won the game!"
            )
        if game.status == GAME_STATUS.LOST:
            raise EndGameException(
                type="GAME_LOST_STATUS", message="Sorry, you are DEAD."
            )

        return Response(
            message="Keep trying!",
            attempts=len(json.loads(game.attempts)),
            feedback=json.loads(game.feedbacks).pop(),
        )
