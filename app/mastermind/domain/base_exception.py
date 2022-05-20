class BaseException(Exception):
    def __init__(self, type: str=None, message: str=None, status: int=400):
        Exception.__init__(self, message)
        self.type = type
        self.message = message
        self.status = status

    def to_dict(self):
        return {
            'type': self.type,
            'message': self.message
        }
