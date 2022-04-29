from abc import ABC, abstractmethod

from entities.post import Post


class CreatePostDAO(ABC):

    @abstractmethod
    def create_post(self, post: Post) -> Post:
        pass

    @abstractmethod
    def create_post_image(self, post_id: int, image: str) -> str:
        pass

    @abstractmethod
    def get_post_image(self, post_id: int) -> str:
        pass
    