from custom_exceptions.group_exceptions import GroupIdNonExistent
from custom_exceptions.group_member_junction_exceptions import WrongType
from custom_exceptions.group_not_found import GroupNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.implementation_classes.group_dao import GroupDAOImp
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from service_layer.implementation_classes.group_service import GroupPostgreService
from unittest.mock import MagicMock, patch
from entities.group import Group

GDI = GroupDAOImp()
GVPD = GroupViewPostgresDao()
GPS = GroupPostgreService(GDI, GVPD)


def test_get_join_group():
    result = GDI.join_group(1,1)
    assert result[0]== 1

def test_service_join_group_wrong_group_id_type():
    try:
        GPS.service_join_group("1", 1)
        assert False
    except WrongType as e:
        assert str(e) == "please enter a number"

def test_service_join_group_no_group_id():
    try:
        GPS.service_join_group(1, 10000)
        assert False
    except UserNotFound as e:
        assert str(e) == 'The user could not be found.'

def test_get_creator():
    result = GDI.get_creator(1)
    assert result[0][0] == 'matt'

def test_service_get_creator():
    GDI.get_creator = MagicMock(return_value='matt')
    result = GPS.service_get_creator(1)
    assert result == 'matt'

def test_service_get_creator_wrong_id_type():
    try:
        GPS.service_get_creator("1")
        assert False
    except WrongType as e:
        assert str(e) == "please enter a number"

def test_service_get_creator_no_id():
    GDI.get_creator = MagicMock(return_value=[])
    try:
        GPS.service_get_creator(12321321)
        assert False
    except GroupIdNonExistent as e:
        assert str(e) == "This Id does not exist"
