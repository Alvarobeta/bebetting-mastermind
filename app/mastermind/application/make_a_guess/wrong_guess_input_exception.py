import os

from app.mastermind.application.application_exception import ApplicationException

class WrongGuessInputException(ApplicationException):
    def __init__(self):
        super().__init__(
            type="wrong_input_number",
            message=f"You must input {os.environ['DEFAULT_CODE_LENGTH']} colours.",
        )