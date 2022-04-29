class GroupMemberJunction:

    def __init__(self, first_name:str, last_name: str, user_id: int, group_id: int):
        self.last_name = last_name
        self.first_name = first_name
        self.group_id = group_id
        self.user_id = user_id

    def make_dictionary(self):
        dictionary = {
            "group_id": self.group_id,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
        return dictionary

    def __str__(self):
        return "user first name {} user last name {} the user ID {} the group id {}".format(self.first_name,
                                                                                            self.last_name,
                                                                                            self.user_id,
                                                                                            self.group_id)

    def __repr__(self):
        return "First name {} Last Name {} User ID {} Group Id {}".format(self.first_name,
                                                                          self.last_name,
                                                                          self.user_id,
                                                                          self.group_id)
