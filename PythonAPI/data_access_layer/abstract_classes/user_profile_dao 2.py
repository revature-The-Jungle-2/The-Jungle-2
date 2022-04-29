from abc import ABC, abstractmethod

from entities.user import User


class UserProfileDAO(ABC):

    @abstractmethod
    def get_user_profile(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_user_image(self, user_id: int) -> str:
        pass

    @abstractmethod
    def update_user_image(self, user_id: int, image: str) -> bool:
        pass

    @abstractmethod
    def update_image_format(self, user_id: int, image_data: str) -> User:
        pass

    @abstractmethod
    def update_first_name(self, user_id: int, first_name: str) -> User:
        pass

    @abstractmethod
    def update_last_name(self, user_id: int, last_name: str) -> User:
        pass

    @abstractmethod
    def update_username(self, user_id: int, username: str) -> User:
        pass

    @abstractmethod
    def update_password(self, user_id: int, password: str) -> User:
        pass

    @abstractmethod
    def update_about_me(self, user_id: int, about_me: str) -> User:
        pass

    @abstractmethod
    def update_birthdate(self, user_id: int, birthdate: str) -> User:
        pass
