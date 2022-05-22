from fastapi_sqlalchemy import db

from app.mastermind.domain.domain_exception import DomainException
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.game_repository import GameRepository
from models import Game as ModelGame


class GameNotFound(DomainException):
    def __init__(self):
        super().__init__(message="Game don't exist", type="game_not_found", status=404)


class GameRepositorySqlAlchemy(GameRepository):
    def get_by_id(self, game_id: str) -> Game:
        game = db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

        if not game:
            raise GameNotFound()

        return game

    def create(self, game: Game) -> Game:
        game_to_db = ModelGame(
            id=game.id,
            code=game.code,
            attempts=game.attempts,
            feedbacks=game.feedbacks,
            status=game.status,
        )

        db.session.add(game_to_db)
        db.session.commit()

        return game

    def save(self, game: Game) -> Game:
        game_from_db = self.get_by_id(game_id=game.id)

        game_from_db.id = game.id
        game_from_db.attempts = game.attempts
        game_from_db.feedbacks = game.feedbacks
        game_from_db.status = game.status

        db.session.add(game_from_db)
        db.session.commit()
        db.session.refresh(game_from_db)

        return game
