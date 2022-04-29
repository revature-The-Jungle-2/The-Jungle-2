from abc import ABC, abstractmethod
from typing import List

from entities.group_post import GroupPost


class GroupPostServiceAbs(ABC):
    @abstractmethod
    def service_create_post(self, post: GroupPost) -> GroupPost:
        pass

    @abstractmethod
    def service_create_post_image(self, image: str) -> bool:
        pass

    @abstractmethod
    def service_get_post_by_id(self, post_id: int) -> GroupPost:
        pass

    @abstractmethod
    def service_get_all_posts(self) -> List[GroupPost]:
        pass

    @abstractmethod
    def service_get_all_posts_by_group_id(self, group_id: int) -> List[GroupPost]:
        pass

    @abstractmethod
    def service_delete_post_by_post_id(self, post_id: int) -> bool:
        pass
