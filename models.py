from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY


Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(ARRAY(String))
    attempts = Column(Integer)
    # guess_history = Column(ARRAY(ARRAY(String)))

    def dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "attempts": self.attempts
        }
