class WrongType(Exception):
    def __init__(self, message):
        self.message = message


class WrongId(Exception):
    def __init__(self, message):
        self.message = message


class Invalid(Exception):
    def __init__(self, message):
        self.message = message


