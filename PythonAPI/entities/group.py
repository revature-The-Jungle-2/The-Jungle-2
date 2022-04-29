class Group:
    def __init__(self,
                 group_id: int = None,  # primary key
                 user_id: int = None,  # the original user that created the group
                 group_name: str = None,  # must be unique
                 group_about: str = None,
                 image_format: str = None,
                 ):

        self.group_id = group_id
        self.user_id = user_id
        self.group_name = group_name
        self.group_about = group_about
        self.image_format = image_format

    def make_dictionary(self):
        dictionary = {
            "groupId": self.group_id,
            "userId": self.user_id,
            "groupName": self.group_name,
            "groupAbout": self.group_about,
            "imageFormat": self.image_format,
            }
        return dictionary

    def __str__(self):
        return f"groupId {self.group_id}, userId {self.user_id}, groupName {self.group_name}, groupAbout{self.group_about}, " \
               f"imageFormat {self.image_format}"
