from typing import List

from data_access_layer.abstract_classes.group_view_dao_abs import GroupViewDao
from entities.group import Group


class GroupViewDaoImp(GroupViewDao):

    dummy_group = Group(1, 12, "Comic Club", "We love superheros", "placeholder")
    dummy_group_two = Group(2, 11, "Soccer Fans", "We Love Futbol", "placeholder")
    group_list = [dummy_group, dummy_group_two]
    group_id_generator = 3

    def get_group_by_id(self, group_id: int) -> Group:
        for group in GroupViewDaoImp.group_list:
            if group.group_id == group_id:
                return group

    def get_all_groups(self) -> List[Group]:
        return GroupViewDaoImp.group_list

    def get_all_groups_by_user_id(self, user_id) -> List[Group]:
        return  GroupViewDaoImp.group_list
