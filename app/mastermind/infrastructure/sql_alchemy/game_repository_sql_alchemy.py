import logging

from fastapi_sqlalchemy import db

from app.mastermind.domain.domain_exception import DomainException
from app.mastermind.domain.entities.game import Game
from app.mastermind.domain.game_repository import GameRepository
from models import Game as ModelGame

logger = logging.getLogger(__name__)

class GameNotFound(DomainException):
    def __init__(self):
        super().__init__(message="Game don't exist", type="game_not_found", status=404)


class GameRepositorySqlAlchemy(GameRepository):
    def get_by_id(self, game_id: str) -> Game:
        logger.debug(f'------- get_by_id()  game id={game_id} -------')
        game = db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

        if not game:
            raise GameNotFound()

        return game

    def save(self, game: Game) -> Game:
        logger.debug(f'------- save() game={game}, game.id={game.id} -------')
        # game.attempts = []
        # game.feedbacks = []
        game_to_db = ModelGame(
            id=game.id,
            code=game.code,
            attempts=game.attempts,
            feedbacks=game.feedbacks,
            status=game.status,
            )
        logger.debug(f'------- game_to_db={game_to_db} -------')
        db.session.add(game_to_db)
        db.session.commit()
        logger.debug(f'------- game updated -------')
        return game
