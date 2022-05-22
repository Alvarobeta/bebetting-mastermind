from app.mastermind.domain.domain_exception import DomainException


class WrongInputException(DomainException):
    def __init__(self, message: str):
        super().__init__(type="WrongInputException", message=message)
