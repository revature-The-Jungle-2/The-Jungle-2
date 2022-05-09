from typing import List
from custom_exceptions.group_not_found import GroupNotFound
from custom_exceptions.user_not_found import UserNotFound
from entities.group import Group
from service_layer.abstract_classes.group_postgres_service_abs import GroupService
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao

class GroupPostgresService(GroupService):

    def __init__(self, group_view_dao: GroupViewPostgresDao):
        self.group_view_dao = group_view_dao

    def service_get_group_by_id(self, group_id: int) -> Group:
        result = self.group_view_dao.get_group_by_id(group_id)
        print(result)
        if result == None:
            raise GroupNotFound("Group not found")
        return result

    def service_get_all_groups(self) -> List[Group]:
        result = self.group_view_dao.get_all_groups()
        if not result:
            raise GroupNotFound("Server error")
        return result

    def service_get_groups_by_user_id(self, user_id: int) -> List[Group]:
        result = self.group_view_dao.get_all_groups_by_user_id(user_id)
        if not result:
            raise UserNotFound("User not found")
        return result
