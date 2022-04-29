from abc import ABC, abstractmethod
from typing import List

from entities.post import Post


class PostFeedDao(ABC):

    @abstractmethod
    def get_all_posts(self) -> List[Post]:
        pass

    @abstractmethod
    def delete_a_post(self, postid: int) -> bool:
        pass

    @abstractmethod
    def get_all_posts_with_user_id(self, user_id: int) -> List[Post]:
        pass
