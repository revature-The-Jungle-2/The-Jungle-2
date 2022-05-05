from custom_exceptions.group_exceptions import NullValues, InputTooShort, InputTooLong, GroupNameTaken, \
    GroupIdNonExistent
from custom_exceptions.group_member_junction_exceptions import WrongType
from custom_exceptions.group_not_found import GroupNotFound
from data_access_layer.implementation_classes.group_dao import GroupDAOImp
from unittest.mock import MagicMock, patch
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from entities.group import Group
from service_layer.implementation_classes.group_service import GroupPostgreService
import random

GDI = GroupDAOImp()
GVPD = GroupViewPostgresDao()
GPS = GroupPostgreService(GDI, GVPD)

fake_groups = Group(0, 1, "Dancer", "We love dancing", "Image")
fake_groups2 = Group(0, 1, "Dancer123", "We love dancing", "Image")


def test_dao_create_group():
    groups = Group(0, 1, "Dancer"+str(random.randint(1,9999)), "We love dancing", "Image")
    result = GDI.create_group(groups)
    assert result.group_id != 0

def test_sl_create_group():
    GVPD.get_all_groups = MagicMock(return_value=[fake_groups])
    groups1 = Group(0, 1, "Dancer" + str(random.randint(1, 9999)), "We love dancing", "Image")
    result = GPS.service_create_group(groups1)
    assert result.image_format == "Image"

def test_sl_name_taken():
    GVPD.get_all_groups = MagicMock(return_value=[fake_groups])
    try:
        GPS.service_create_group(fake_groups)
        assert False
    except GroupNameTaken as e:
        assert str(e) == "The group name you entered is already taken! Please try another group name."

def test_sl_nullvalue_group_name():
    groupdata = Group(0, 1, "", "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except NullValues as e:
        assert str(e) == "You must fill in all inputs!"
#
def test_sl_too_short_group_name():
    groupdata = Group(0, 1, "Da", "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooShort as e:
        assert str(e) == "Group name should be at least three characters long!"
#
def test_sl_too_long_group_name():
    groupdata = Group(0, 1, "Dancer"*40, "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooLong as e:
        assert str(e) == "You have exceeded the 40-character limit!"
#
def test_sl_too_long_group_about():
    groupdata = Group(0, 1, "Dancers", "500"*500, "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooLong as e:
        assert str(e) == "You have exceeded the 500-character limit!"
#
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
        GPS.service_join_group(100000, 1)
        assert False
    except GroupNotFound as e:
        assert str(e) == 'The group could not be found.'

def test_get_creator():
    result = GDI.get_creator(1)
    assert result[0][0] == 'John'

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