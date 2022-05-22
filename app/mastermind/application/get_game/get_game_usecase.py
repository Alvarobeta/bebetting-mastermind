from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.game_repository import GameRepository


class GetGameUseCase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, game_id: str) -> Game:
        game = self.gameRepository.get_by_id(game_id)
        return game
