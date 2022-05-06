from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from entities.group_post import GroupPost

GPImp = GroupPostDAO()

test_group = GroupPost(1, 4, 1, "text", "image format", 0, "2022-05-05 19:30:21.117")


# https://placebeard.it/640x360
def test_create_post_success():
    GPImp.create_post(test_group)
    result = GPImp.create_post.(test_group)
    assert result == test_group


def test_create_post_id_zero_fail():
    GPImp.create_post(GroupPost(0, 1, 1, "a", "gif", ))


# InvalidInput

def test_create_post_post_id_not_int_fail():
    pass


# WrongTypeInput

def test_create_post_no_input_given_fail():
    pass


# InputTooLong >500

def test_create_post_image_success():
    pass


def test_create_post_image_image_not_found_fail():
    pass


def test_get_post_by_id_success():
    pass


def test_get_post_by_id_no_id_found_fail():
    pass


def test_get_all_posts_success():
    pass


def test_get_all_posts_no_posts_found_fail():
    pass


def test_get_all_posts_by_group_id_success():
    pass


def test_get_all_posts_by_group_id_group_id_not_found():
    pass


def test_get_all_posts_by_group_id_fail():
    pass


def test_delete_post_by_post_id_success():
    pass


# boolean

def test_delete_post_by_post_id_fail():
    pass
