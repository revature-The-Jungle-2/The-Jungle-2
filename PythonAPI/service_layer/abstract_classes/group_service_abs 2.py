from abc import ABC, abstractmethod
from entities.group import Group


class GroupService(ABC):
    @abstractmethod
    def service_create_group(self, group: Group):
        pass

    @abstractmethod
    def service_join_group(self, group_id: int, user_id: int):
        pass
