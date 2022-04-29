from abc import ABC, abstractmethod

from entities.group import Group


class GroupDAO(ABC):
    @abstractmethod
    def create_group(self, group: Group) -> Group:
        pass

    @abstractmethod
    def join_group(self, group_id: int, user_id: int):
        pass

    @abstractmethod
    def get_creator(self, group_id: int):
        pass
