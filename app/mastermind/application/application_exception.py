class ApplicationException(Exception):
    def __init__(self, type: str, message: str, status: int = 400):
        Exception.__init__(self, message)
        self.type = type
        self.message = message
        self.status = status

    def to_dict(self):
        return {"msg": self.message, "type": self.type}
