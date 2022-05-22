from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, Enum
from sqlalchemy.dialects import postgresql

from app.mastermind.domain.entities.game import GAME_STATUS


Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, index=True)
    code = Column(ARRAY(String))
    attempts = Column(postgresql.ARRAY(String))
    status = Column(Enum(GAME_STATUS))
    feedbacks = Column(postgresql.ARRAY(String))

    def dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "attempts": self.attempts,
            "status": self.status,
            "feedbacks": self.feedbacks,
        }
