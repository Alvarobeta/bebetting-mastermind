from dataclasses import dataclass

from app.mastermind.domain.entities.game import Game


@dataclass
class GetGameResponse:
    game: Game
