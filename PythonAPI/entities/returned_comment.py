class ReturnedComment:
    def __init__(self,
                 comment_id: int = None,  # primary key
                 post_id: int = None,  # foreign key
                 user_id: int = None,  # foreign key
                 group_id: int = None,
                 reply_user: int = None,
                 comment_text: str = None,
                 likes: int = None,  # not in the user stories but included as a stretch
                 date_time_of_creation: str = None,
                 user_name: str = None
                 ):
        self.comment_id = comment_id
        self.post_id = post_id
        self.user_id = user_id
        self.group_id = group_id
        self.reply_user = reply_user
        self.comment_text = comment_text
        self.likes = likes
        self.date_time_of_creation = date_time_of_creation
        self.user_name = user_name

    def make_dictionary(self):
        dictionary = {
            "comment_id": self.comment_id,
            "post_id": self.post_id,
            "user_id": self.user_id,
            "group_id": self.group_id,
            "reply_user": self.reply_user,
            "comment_text": self.comment_text,
            "likes": self.likes,
            "date_time_of_creation": self.date_time_of_creation,
            "user_name": self.user_name
        }
        return dictionary
