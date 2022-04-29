class PostNotFound(Exception):
    def __init__(self, message):
        self.message = message


class InvalidInput(Exception):
    def __init__(self, message):
        self.message = message


class InputTooLong(Exception):
    def __init__(self, message):
        self.message = message


class NoInputGiven(Exception):
    def __init__(self, message):
        self.message = message


class WrongTypeInput(Exception):
    def __init__(self, message):
        self.message = message
