import code
import logging
import json

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

        logger.debug(f'------- get_by_id() gameid={game_id} -------')
        game = db.session.query(ModelGame).filter(ModelGame.id == game_id).first()

        logger.debug(f'------- get_by_id() game={game}, gameid={game.id} -------')

        if not game:
            raise GameNotFound()
        logger.debug(f'------- returning game -------')

        return game

    def create(self, game: Game) -> Game:
        logger.debug(f'------- create() game={game} -------')

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
        logger.debug(f'------- game created -------')
        return game
    
    def save(self, game: Game) -> Game:
        logger.debug(f'------- save() game={game} -------')
        logger.debug(f'------- save() game attempts type={type(game.attempts)} -------')
        
        game_from_db = self.get_by_id(game_id=game.id)
        #serialize attempts to json
        #logger.debug(f'------- SERIALIZING ATTEMPTS -------')
        # if type(game.attempts) == list:
        #     game_from_db.attempts = json.dumps(game.attempts)
            
        game_from_db.id = game.id
        game_from_db.attempts=game.attempts
        game_from_db.feedbacks=game.feedbacks
        game_from_db.status=game.status

        logger.debug(f'--------------------------------------------------------------- ')
        logger.debug(f'------- before modified: game_to_db id={game_from_db.id}-------')
        logger.debug(f'------- before modified: game_to_db code={game_from_db.code}-------')
        logger.debug(f'------- before modified: game_to_db attempts={game_from_db.attempts}-------')
        logger.debug(f'------- before modified: game_to_db feedbacks={game_from_db.feedbacks}-------')
        logger.debug(f'------- before modified: game_to_db status={game_from_db.status}-------')
        logger.debug(f'--------------------------------------------------------------- ')

        db.session.add(game_from_db)
        db.session.commit()
        db.session.refresh(game_from_db)

        logger.debug(f'------- game updated -------')

        return game
