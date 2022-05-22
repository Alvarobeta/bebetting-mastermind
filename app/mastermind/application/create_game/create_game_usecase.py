import logging
from dataclasses import dataclass
import uuid

from app.mastermind.application.create_game.create_game_dto import \
    CreateGameDto
from app.mastermind.domain.game_repository import GameRepository
from app.mastermind.domain.entities.game import Game
# from models import Game

logger = logging.getLogger(__name__)


@dataclass
class CreateGameUsecase:
    def __init__(self, gameRepository: GameRepository) -> None:
        self.gameRepository = gameRepository

    def __call__(self, createGameDto: CreateGameDto) -> Game:
        game = Game(code=createGameDto.code)
        self.gameRepository.create(game)

        return game
