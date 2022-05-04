from custom_exceptions.post_exceptions import PostNotFound
from custom_exceptions.post_id_non_existent import PostIdNonExistent
from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
from entities.post import Post
from service_layer.implementation_classes.postfeed_service import PostFeedServiceImp
from unittest.mock import MagicMock

PFDAO = PostFeedDaoImp()
PFSImp = PostFeedServiceImp(PFDAO)
test_feed_good = Post(1, 1, 2, "My cat", "jpeg", 1, "2022-05-03 15:56:20.814")


def test_service_get_all_posts():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[1])
        result = PFSImp.get_all_posts_service()
        assert result[0] >= 1
    except PostNotFound as e:
        assert str(e) == 'Id not found, please try again'


def test_get_all_posts_no_post_found():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[999])
        result = PFSImp.get_all_posts_service()
        assert result[999] != 0
    except PostNotFound as e:
        assert str(e) == 'Post Id not found, please try again'


def test_service_delete_a_post():
    try:
        PFSImp.post_feed_dao.delete_a_post = MagicMock(
            return_value=[Post(1, 1, 2, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")])
        PFSImp.delete_a_post_service(1)
        assert True
    except PostIdNonExistent as e:
        assert str(e) == "Id not found, please try again."


def test_delete_a_post_no_post_id_found():
    try:
        PFSImp.delete_a_post_service = MagicMock(
            return_value=[Post(999, 1, 2, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")])
        PFSImp.delete_a_post_service(999)
        assert False
    except PostNotFound as e:
        assert str(e) == 'Id not found, please try again.'


def test_service_get_all_posts_with_user_id():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[test_feed_good])
        result = PFSImp.get_all_posts_service(test_feed_good.user_id)
        assert result[0]['user_id'] == 1
    except PostIdNonExistent as e:
        assert str(e) == 'Id not found, please try again'


def test_get_all_posts_no_id_found():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[test_feed_good])
        result = PFSImp.get_all_posts_service(test_feed_good.user_id)
        assert result[0]['user_id'] == 0
    except PostIdNonExistent as e:
        assert str(e) == 'Id not found, please try again.'