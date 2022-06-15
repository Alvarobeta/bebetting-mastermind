from dataclasses import dataclass

from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.game_repository import GameRepository


@dataclass
class CreateGameUsecase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self) -> Game:
        game = Game()
        self.gameRepository.create(game)

        return game
