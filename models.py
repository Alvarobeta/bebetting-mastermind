from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ARRAY, Enum

from app.mastermind.domain.entities.game import GAME_STATUS


Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, index=True)
    code = Column(ARRAY(String))
    attempts = Column(String)
    status = Column(Enum(GAME_STATUS))
    feedbacks = Column(String)

    def dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "attempts": self.attempts,
            "status": self.status,
            "feedbacks": self.feedbacks,
        }
