from unittest.mock import MagicMock
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from entities.group_post import GroupPost
from service_layer.implementation_classes.group_post_service import GroupPostService

gpdao = GroupPostDAO()
GroupSL = GroupPostService(gpdao)
test_group = GroupPost(1, 1, 1, 'test', 'test', 0, 'test')


def test_service_create_post_success():
    result = gpdao.create_post = MagicMock(test_group)
    assert result == test_group


def test_service_create_post_id_zero_fail():
    # try:
    # # GPImp.create_post(GroupPost(0, 1, 1, "a", "gif", ))
    pass


# InvalidInput

def test_service_create_post_post_id_not_int_fail():
    pass


# WrongTypeInput

def test_service_create_post_no_input_given_fail():
    pass


# InputTooLong >500

def test_service_create_post_image_success():
    pass


def test_service_create_post_image_image_not_found_fail():
    pass


def test_service_get_post_by_id_success():
    pass


def test_service_get_post_by_id_no_id_found_fail():
    pass


def test_service_get_all_posts_success():
    pass


def test_service_get_all_posts_no_posts_found_fail():
    pass


def test_service_get_all_posts_by_group_id_success():
    pass


def test_service_get_all_posts_by_group_id_group_id_not_found():
    pass


def test_service_get_all_posts_by_group_id_fail():
    pass


def test_service_delete_post_by_post_id_success():
    pass


# boolean

def test_service_delete_post_by_post_id_fail():
    pass
