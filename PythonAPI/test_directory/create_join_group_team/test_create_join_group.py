from custom_exceptions.group_exceptions import NullValues, InputTooShort, InputTooLong, GroupNameTaken
from custom_exceptions.group_name_already_taken import GroupNameAlreadyTaken
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
    result = GPS.service_create_group(fake_groups2)
    assert result.group_name == "Dancer123"


def test_sl_name_taken():
    GVPD.get_all_groups = MagicMock(return_value =[fake_groups])
    try:
        GDI.create_group(fake_groups)
        assert False
    except GroupNameAlreadyTaken as e:
        assert str(e) == "That group name has already been taken."


def test_sl_nullvalue_group_name():
    groupdata = Group(0, 1, "", "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except NullValues as e:
        assert str(e) == "You must fill in all inputs!"

def test_sl_too_short_group_name():
    groupdata = Group(0, 1, "Da", "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooShort as e:
        assert str(e) == "Group name should be at least three characters long!"

def test_sl_too_long_group_name():
    groupdata = Group(0, 1, "Dancer"*40, "We love Dancing", "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooLong as e:
        assert str(e) == "You have exceeded the 40-character limit!"

def test_sl_too_long_group_about():
    groupdata = Group(0, 1, "Dancers", "500"*500, "image")
    try:
        GPS.service_create_group(groupdata)
        assert False
    except InputTooLong as e:
        assert str(e) == "You have exceeded the 500-character limit!"




