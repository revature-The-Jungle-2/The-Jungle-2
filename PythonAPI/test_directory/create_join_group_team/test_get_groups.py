from unittest.mock import MagicMock
from custom_exceptions.group_exceptions import GroupIdNonExistent
from custom_exceptions.group_not_found import GroupNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from entities.group import Group
from service_layer.implementation_classes.group_postgres_service import GroupPostgresService

GVPD = GroupViewPostgresDao()
GPS = GroupPostgresService(GVPD)
test_group = Group(1,1,'test','test','test')


def test_dao_get_group_by_id():
    result = GVPD.get_group_by_id(1)
    assert result.group_id == 1

def test_dao_get_all_groups():
    result = GVPD.get_all_groups()
    assert result[0].group_id == 1

def test_dao_get_all_groups_by_user_id():
    result = GVPD.get_all_groups_by_user_id(1)
    assert result[0].group_id == 1

def test_sl_get_group_by_id():
    GVPD.get_group_by_id = MagicMock(return_value=test_group)
    result = GPS.service_get_group_by_id(1)
    assert result.group_id == 1

def test_sl_get_all_groups():
    GVPD.get_all_groups = MagicMock(return_value=[test_group])
    result = GPS.service_get_all_groups()
    assert result[0].group_id == 1

def test_sl_get_all_groups_by_user_id():
    GVPD.get_all_groups_by_user_id = MagicMock(return_value=[test_group])
    result = GPS.service_get_groups_by_user_id(1)
    assert result[0].group_id == 1

def test_sl_get_group_by_no_id():
    GVPD.get_group_by_id = MagicMock(return_value=None)
    try:
        GPS.service_get_group_by_id(11111111)
        assert False
    except GroupNotFound as e:
        assert str(e) == "Group not found"

def test_sl_get_all_groups_server_error():
    GVPD.get_all_groups = MagicMock(return_value=[])
    try:
        GPS.service_get_all_groups()
        assert False
    except GroupNotFound as e:
        assert str(e) == "Server error"

def test_sl_get_all_groups_by_no_user_id():
    GVPD.get_all_groups_by_user_id = MagicMock(return_value=[])
    try:
        GPS.service_get_groups_by_user_id(1)
        assert False
    except UserNotFound as e:
        assert str(e) == "User not found"


