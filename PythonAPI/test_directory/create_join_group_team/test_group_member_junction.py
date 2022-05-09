from unittest.mock import MagicMock

from data_access_layer.implementation_classes.group_dao import GroupDAOImp
from data_access_layer.implementation_classes.group_member_junction_dao import GroupMemberJunctionDao
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from entities.group_member_junction import GroupMemberJunction
from service_layer.implementation_classes.group_member_junction_service import GroupMemberJunctionService
from service_layer.implementation_classes.group_service import GroupPostgreService

GMJD = GroupMemberJunctionDao()
GMJS = GroupMemberJunctionService(GMJD)
GDI = GroupDAOImp()
GPD = GroupViewPostgresDao()
GPS = GroupPostgreService(GDI, GPD)
GPS.service_join_group(1,1)


test_member = GroupMemberJunction('John','Thomson', 1, 1)


def test_dao_get_all_users_in_a_group():

    result = GMJD.get_all_users_in_a_group(1)
    assert result[0].group_id == 1

def test_dao_leave_group():
    user_ls = GMJD.get_all_users_in_a_group(1)
    test_id = user_ls[0].user_id
    result = GMJD.leave_group(test_id, 1)
    assert result == True

def test_sl_get_all_users_in_a_groups():
    GMJD.get_all_users_in_a_group = MagicMock(return_value=[test_member])
    result = GMJS.get_all_users_in_a_group(1)
    assert result[0].group_id == 1

def test_sl_leave_group():
    GMJD.leave_group = MagicMock(return_value=True)
    result = GMJS.leave_group(1, 1)
    assert result == True