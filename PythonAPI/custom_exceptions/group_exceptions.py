class GroupIdNonExistent(Exception):
    def __init__(self, message):
        self.message = message


class InputTooLong(Exception):
    def __init__(self, message):
        self.message = message


class InputTooShort(Exception):
    def __init__(self, message):
        self.message = message


class NullValues(Exception):
    def __init__(self, message):
        self.message = message


class UserIdNonExistent(Exception):
    def __init__(self, message):
        self.message = message


class GroupNameTaken(Exception):
    def __init__(self, message):
        self.message = message
