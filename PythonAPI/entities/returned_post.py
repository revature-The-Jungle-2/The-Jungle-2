class ReturnedPost:
    def __init__(self,
                 post_id: int = None,  # primary key
                 user_id: int = None,  # foreign key
                 group_id: int = None,  # foreign key
                 post_text: str = None,
                 image_format: str = None,
                 likes: int = None,
                 date_time_of_creation: str = None,
                 user_name: str = None
                 ):
        self.post_id = post_id
        self.user_id = user_id
        self.group_id = group_id
        self.post_text = post_text
        self.image_format = image_format
        self.likes = likes
        self.date_time_of_creation = date_time_of_creation
        self.user_name = user_name

    def make_dictionary(self):
        dictionary = {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "group_id": self.group_id,
            "post_text": self.post_text,
            "image_data": self.image_format,
            "likes": self.likes,
            "date_time_of_creation": self.date_time_of_creation,
            "user_name": self.user_name
        }
        return dictionary
