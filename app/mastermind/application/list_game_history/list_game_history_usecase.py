import logging
import json
from typing import List
from app.mastermind.application.list_game_history.list_game_history_response import ListGameHistoryResponse
from pydantic import BaseModel

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.game_repository import GameRepository

logger = logging.getLogger(__name__)

# class Responsess(BaseModel):
#     history: List[List[str]]


class ListGameHistoryUseCase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, game_id: str) -> ListGameHistoryResponse:
        game = self.gameRepository.get_by_id(game_id=game_id)
        a = json.loads(game.attempts)

        return ListGameHistoryResponse(history = a)
