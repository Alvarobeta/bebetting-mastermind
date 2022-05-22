import logging
from typing import List

from app.mastermind.domain.entities.guess_colour import GuessColour
from app.mastermind.domain.game_repository import GameRepository

logger = logging.getLogger(__name__)


class ListGameHistoryUseCase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, game_id: str) -> List[List[GuessColour]]:
        game = self.gameRepository.get_by_id(game_id)
        return game.attempts
