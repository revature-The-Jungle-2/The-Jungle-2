from custom_exceptions import postIdNonExistent
from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
from entities.post import Post
from service_layer.implementation_classes.postfeed_service import PostFeedServiceImp
from unittest.mock import MagicMock, Mock
from psycopg import OperationalError

PFDAO = PostFeedDaoImp()
PFSImp = PostFeedServiceImp(PFDAO)
test_feed_good = Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")


def test_service_get_all_posts():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[])
        result = PFSImp.get_all_posts_service()
        assert result[0][0] >= 2
    except postIdNonExistent as e:
        assert str(e) == 'Id not found, please try again'

def test_get_all_posts_no_post_found():


def test_service_delete_a_post():
    try:
        PFSImp.post_feed_dao.delete_a_post = MagicMock(
            return_value=[Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")])
        PFSImp.delete_a_post_service(1)
        assert False
    except postIdNonExistent as e:
        assert str(e) == "Id not found, please try again."

def test_delete_a_post_no_post_id_found():

def test_service_get_all_posts_with_user_id():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[test_feed_good])
        result = PFSImp.get_all_posts_service(test_feed_good.user_id)
        assert result[0]['user_id'] == -1
    except postIdNonExistent as e:
        assert str(e) == 'Id not found, please try again'

def test_get_all_posts_no_id_found():

