from abc import ABC, abstractmethod

from entities.user import User


class UserProfileDAO(ABC):

    @abstractmethod
    def get_user_profile(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update_user_profile(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_image(self, user_id: int) -> str:
        pass

    @abstractmethod
    def update_user_image(self, user_id: int, image: str) -> str:
        pass

    @abstractmethod
    def update_user_image_format(self, user_id: int, image_data: str) -> User:
        pass

    @abstractmethod
    def update_password(self, user_id: int, password: str) -> User:
        """Stretch"""
        pass

    @abstractmethod
    def get_user_followers(self, user_id: int) -> dict[str:int]:
        """Stretch"""
        pass

    @abstractmethod
    def get_users_following_user(self, user_id: int) -> dict[str:int]:
        """Stretch"""
        pass

    @abstractmethod
    def follow_user(self, user_follower_id: int, user_being_followed_id: int) -> bool:
        pass

    @abstractmethod
    def unfollow_user(self, user_follower_id: int, user_being_followed_id: int) -> bool:
        pass
