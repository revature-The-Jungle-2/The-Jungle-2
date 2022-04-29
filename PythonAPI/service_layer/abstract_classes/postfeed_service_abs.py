from abc import ABC, abstractmethod


class PostfeedService(ABC):

    @abstractmethod
    def get_all_posts_service(self):
        pass

    @abstractmethod
    def get_all_posts_by_user_id_service(self, userid: int):
        pass

    @abstractmethod
    def delete_a_post_service(self, postid: int):
        pass
