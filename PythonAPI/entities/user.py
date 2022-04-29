class User:
    def __init__(self,
                 user_id: int = 'default',  # primary key
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None,
                 username: str = None,  # must be unique
                 passcode: str = None,
                 user_about: str = None,
                 user_birth_date: str = None,
                 user_image_format: str = None
                 ):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.passcode = passcode
        self.user_about = user_about
        self.user_birth_date = user_birth_date
        self.user_image_format = user_image_format

    def make_dictionary(self):
        dictionary = {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username,
            "passcode": self.passcode,
            "user_about": self.user_about,
            "user_birth_date": self.user_birth_date,
            "user_image_format": self.user_image_format
            }
        return dictionary

    def __str__(self):
        return f"user_id: {self.user_id},first_name: {self.first_name},last_name: {self.last_name}, " \
               f"email: {self.email}, username: {self.username}, passcode: ********, user_about: {self.user_about}," \
               f"user_birth_date: {self.user_birth_date},user_image_format: {self.user_image_format}"
