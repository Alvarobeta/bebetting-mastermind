# from sqlalchemy.orm import Session

import logging

# from app.mastermind.infrastructure.FastAPI.api_v1.wrong_input_exception import \
#     WrongInputException
# from app.mastermind.domain.entities.game import Game
# from models import Guessing as ModelGuessing
# from schema import Guessing as SchemaGuessing

logger = logging.getLogger(__name__)


# def get_game(game_id: int):
#     return db.session.query(ModelGame).filter(ModelGame.id == game_id).first()


# def get_game_guessing_historical(game_id: int):
#     return (
#         db.session.query(ModelGuessing).filter(ModelGuessing.owner_id == game_id).all()
#     )


# def create_game(game: SchemaGame):
#     if len(game.code) != int(os.environ["DEFAULT_CODE_LENGTH"]) or any(
#         GuessColour.EMPTY == c for c in game.code
#     ):
#         raise WrongInputException()

#     db_game = ModelGame(
#         code=game.code,
#         attempts=0,
#     )

#     db.session.add(db_game)
#     db.session.commit()

#     return db_game


# def update_game(game: SchemaGame):
#     db.session.add(game)
#     db.session.commit()
#     db.session.refresh(game)


# def create_game_guessing(guessing: SchemaGuessing):
#     db_guessing = ModelGuessing(**guessing.dict())
#     db.session.add(db_guessing)
#     db.session.commit()
#     db.session.refresh(db_guessing)

#     return db_guessing
