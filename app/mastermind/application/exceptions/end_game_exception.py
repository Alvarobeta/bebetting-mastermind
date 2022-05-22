from app.mastermind.domain.domain_exception import DomainException


class EndGameException(DomainException):
    def __init__(self, message: str, type: str = "EndGameException"):
        super().__init__(type=type, message=message)
