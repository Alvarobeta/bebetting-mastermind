from dataclasses import dataclass

from app.mastermind.application.create_game.create_game_dto import \
    CreateGameDto
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.game_repository import GameRepository


@dataclass
class CreateGameUsecase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, createGameDto: CreateGameDto) -> Game:
        game = Game(code=createGameDto.code)
        self.gameRepository.create(game)

        return game
