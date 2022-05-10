from custom_exceptions.group_exceptions import NullValues
from custom_exceptions.post_exceptions import NoInputGiven, PostNotFound
from custom_exceptions.post_id_non_existent import PostIdNonExistent
from custom_exceptions.post_image_not_found import PostImageNotFound
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from entities.group_post import GroupPost

GPImp = GroupPostDAO()

test_group = GroupPost(1, 4, 1, "text", "image format", 0, "2022-05-05 19:30:21.117")


def test_create_post_success():
    GPImp.create_post(test_group)
    result = GPImp.create_post(test_group)
    assert result == test_group


def test_create_post_no_input_given_fail():
    try:
        GPImp.create_post(GroupPost())
        result = GPImp.create_post(GroupPost())
        assert result != GPImp.create_post(GroupPost())
    except NoInputGiven as e:
        assert str(e) == "The post input can not be empty."


def test_create_post_image_success():
    result = GPImp.create_post_image(10, "http://placebeard.it/g/260/180")
    assert result == "http://placebeard.it/g/260/180"


def test_create_post_image_image_not_found_fail():
    try:
        result = GPImp.create_post_image(999999, "http://placebeard.it/g/260/180")
    except PostNotFound as e:
        assert str(e) == "The post could not be found."


def test_get_post_by_id_success():
    result = GPImp.get_post_by_id(1)
    assert result.post_id == 1


# def test_get_post_by_id_no_id_found_fail():
#     try:
#         result = GPImp.get_post_by_id(999)
#         assert result.post_id != 999
#     except PostIdNonExistent as e:
#         assert str(e) == "The id is non existent!"


def test_get_all_posts_success():
    result = GPImp.get_all_posts()
    assert result.__len__() >= 1


def test_get_all_posts_no_posts_found_fail():
    pass


def test_get_all_posts_by_group_id_success():
    result = GPImp.get_all_posts_by_group_id(1)
    assert result.__len__() >= 1


def test_get_all_posts_by_group_id_group_id_not_found_fail():
    try:
        result = GPImp.get_all_posts_by_group_id(10)
        assert result != 10
    except NullValues as e:
        assert str(e) == "There are no posts in this group."


def test_delete_post_by_post_id_success():
    GPImp.delete_post_by_post_id(45)
    assert True

# boolean


# def test_delete_post_by_post_id_fail():
#     pass
