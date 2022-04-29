from typing import List

from data_access_layer.implementation_classes.group_member_junction_dao import GroupMemberJunctionDao
from entities.group_member_junction import GroupMemberJunction
from service_layer.abstract_classes.group_member_junction_service_abs import GroupMemberJunctionServiceAbs
from custom_exceptions.group_member_junction_exceptions import *


class GroupMemberJunctionService(GroupMemberJunctionServiceAbs):
    def __init__(self, group_member_junction_dao: GroupMemberJunctionDao):
        self.group_member_junction_dao = group_member_junction_dao

    def get_all_users_in_a_group(self, group_id) -> List[GroupMemberJunction]:
        return self.group_member_junction_dao.get_all_users_in_a_group(group_id)

    def leave_group(self, user_id: int, group_id: int):
        return self.group_member_junction_dao.leave_group(user_id,group_id)
