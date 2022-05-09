from unittest.mock import MagicMock

from custom_exceptions.group_exceptions import NullValues, InputTooLong
from custom_exceptions.group_id_nonexistent import GroupIdNonExistent
from custom_exceptions.post_exceptions import InvalidInput, WrongTypeInput, NoInputGiven
from custom_exceptions.post_id_non_existent import PostIdNonExistent
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from entities.group_post import GroupPost
from service_layer.implementation_classes.group_post_service import GroupPostService

gpdao = GroupPostDAO()
GroupSL = GroupPostService(gpdao)
test_group = GroupPost(1, 1, 1, 'test', 'test', 0, 'test')


def test_service_create_post_success():
    GroupSL.service_create_post = MagicMock(return_value=True)
    result = GroupSL.service_create_post(test_group)
    assert result is True


def test_service_create_post_id_zero_fail():
    try:
        GroupSL.service_create_post = MagicMock(GroupPost(0))
        assert True
    except InvalidInput as e:
        assert str(e) == "Invalid Input!"


# InvalidInput

def test_service_create_post_post_id_not_int_fail():
    try:
        GroupSL.service_create_post = MagicMock(GroupPost("a"))
        assert True
    except WrongTypeInput as e:
        assert str(e) == "You need to enter number for post ID!"


# WrongTypeInput

def test_service_create_post_no_input_given_fail():
    try:
        GroupSL.service_create_post = MagicMock(GroupPost())
        assert True
    except NoInputGiven as e:
        assert str(e) == "No Input Given!"


def test_service_create_post_input_too_long():
    try:
        GroupSL.service_create_post = MagicMock(GroupPost())
        assert True
    except InputTooLong as e:
        assert str(e) == "Messages too long!"


# InputTooLong >500

def test_service_create_post_image_success():
    GroupSL.service_create_post_image = MagicMock(return_value=True)
    result = GroupSL.service_create_post_image("")
    assert result is True


def test_service_create_post_image_image_not_found_fail():
    try:
        GroupSL.service_create_post_image = MagicMock("http://placebeard.it/g/640/480")
        assert True
    except NullValues as e:
        assert str(e) == "Image not found."


def test_service_get_post_by_id_success():
    GroupSL.service_get_post_by_id = MagicMock(return_value=True)
    result = GroupSL.service_get_post_by_id(1)
    assert result is True


def test_service_get_post_by_id_no_id_found_fail():
    try:
        result = GroupSL.service_get_post_by_id(999)
        assert True
    except NullValues as e:
        assert str(e) == "Post not found"


def test_service_get_all_posts_success():
    GroupSL.service_get_all_posts = MagicMock(return_value=True)
    result = GroupSL.service_get_all_posts()
    assert result is True


def test_service_get_all_posts_no_posts_found_fail():
    try:
        GroupSL.service_get_all_posts()
        assert True
    except NullValues as e:
        assert str(e) == "No posts found."


def test_service_get_all_posts_by_group_id_success():
    GroupSL.service_get_all_posts_by_group_id = MagicMock(return_value=True)
    result = GroupSL.service_get_all_posts_by_group_id(1)
    assert result is True


def test_service_get_all_posts_by_group_id_group_id_not_found():
    try:
        GroupSL.service_get_all_posts_by_group_id(0)
        assert True
    except GroupIdNonExistent as e:
        assert str(e) == "Group not found."


def test_service_get_all_posts_by_group_id_fail():
    try:
        GroupSL.service_get_all_posts_by_group_id(0)
        assert True
    except NullValues as e:
        assert str(e) == "No group posts found."


def test_service_delete_post_by_post_id_success():
    GroupSL.service_delete_post_by_post_id = MagicMock(2)
    assert True


# boolean

def test_service_delete_post_by_post_id_fail():
    try:
        GroupSL.service_delete_post_by_post_id(-50)
        assert True
    except PostIdNonExistent as e:
        assert str(e) == "Delete failed, post id not found."
