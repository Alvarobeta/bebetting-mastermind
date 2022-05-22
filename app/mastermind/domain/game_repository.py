from abc import ABC, abstractmethod

from app.mastermind.domain.entities.game import Game


# puerto
class GameRepository(ABC):
    @abstractmethod
    def get_by_id(self, game_id: str) -> Game:
        pass
    
    @abstractmethod
    def create(self, game: Game) -> Game:
        pass
    
    @abstractmethod
    def save(self, game: Game) -> Game:
        pass
