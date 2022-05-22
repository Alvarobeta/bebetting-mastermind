import json

from app.mastermind.application.list_game_history.list_game_history_response import \
    ListGameHistoryResponse
from app.mastermind.domain.game_repository import GameRepository


class ListGameHistoryUseCase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, game_id: str) -> ListGameHistoryResponse:
        game = self.gameRepository.get_by_id(game_id=game_id)
        a = json.loads(game.attempts)

        return ListGameHistoryResponse(history=a)
