class Creator:
    def __init__(self,first_name,last_name,username):
        self.username = username
        self.last_name = last_name
        self.first_name = first_name

    def dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username
        }