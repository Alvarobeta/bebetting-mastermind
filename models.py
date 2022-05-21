from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(ARRAY(String))
    attempts = Column(Integer)
    
    # guessings = relationship("Guessing", back_populates="owner")

    def dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "attempts": self.attempts
        }

# class Guessing(Base):
#     __tablename__ = "guessings"

#     id = Column(Integer, primary_key=True, index=True)
#     code = Column(ARRAY(String))
#     owner_id = Column(Integer, ForeignKey("games.id"))

#     owner = relationship("Games", back_populates="guessings")

#     def dict(self):
#         return {
#             "id": self.id,
#             "code": self.code,
#             "owner_id": self.owner_id
#         }