from abc import ABC, abstractmethod
from typing import List

from entities.group import Group


class GroupService(ABC):

    @abstractmethod
    def service_get_group_by_id(self, group_id: int) -> Group:
        pass

    @abstractmethod
    def service_get_all_groups(self) -> List[Group]:
        pass

    @abstractmethod
    def service_get_groups_by_user_id(self, user_id: int) -> List[Group]:
        pass