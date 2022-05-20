import os

from app.mastermind.infrastructure.infrastructure_exception import InfrastructureException


class WrongInputException(InfrastructureException):
    def __init__(self):
        super().__init__(
            type="wrong_input_number",
            message=f"You must input {os.environ['DEFAULT_CODE_LENGTH']} valid colours.",
        )
