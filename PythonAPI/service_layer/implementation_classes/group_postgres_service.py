from typing import List

from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from entities.group import Group
from service_layer.abstract_classes.group_postgres_service_abs import GroupService


class GroupPostgresService(GroupService):

    def __init__(self, group_view_dao: GroupViewPostgresDao):
        self.group_view_dao = group_view_dao

    def service_get_group_by_id(self, group_id: int) -> Group:
        return self.group_view_dao.get_group_by_id(group_id)

    def service_get_all_groups(self) -> List[Group]:
        return self.group_view_dao.get_all_groups()

    def service_get_groups_by_user_id(self, user_id: int) -> List[Group]:
        return self.group_view_dao.get_all_groups_by_user_id(user_id)
