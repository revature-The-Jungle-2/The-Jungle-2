class Event:
    def __init__(self,
                 event_id: int = None,  # primary key
                 user_id: int = None,  # the original user that created the event
                 event_name: str = None,  # must be unique
                 event_about: str = None,
                 event_image_data: str = None,
                 event_members: list[str] = None,
                 event_datetime: str = None
                 ):

        self.event_id = event_id
        self.user_id = user_id
        self.event_name = event_name
        self.event_about = event_about
        self.event_image_data = event_image_data
        self.event_members = event_members
        self.event_datetime = event_datetime

    def make_dictionary(self):
        dictionary = {
            "event_id": self.event_id,
            "user_id": self.user_id,
            "event_name": self.event_name,
            "event_about": self.event_about,
            "event_image_data": self.event_image_data,
            "event_members": self.event_members,
            "event_datetime": self.event_datetime
            }
        return dictionary
