from custom_exceptions.post_exceptions import PostNotFound

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


def test_service_delete_a_post():


def get_all_posts(self) -> List[Post]:
    try:
        PFSImp.post_feed_dao.get_all_posts() = MagicMock(
        return List[Post]
    except:
        PostNotFound as e:
            assert str(e) == "No posts found"


def test_service_get_all_posts():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[test_feed_good])
        result = PFSImp.get_all_posts_service(test_feed_good)
        assert result[0]['user_id'] == -1
    except postIdNonExistent as e:
        assert str(e) == 'Id not found, please try again'

def test_service_get_all_posts_with_user_id():
    try:
        PFSImp.get_all_posts_service = MagicMock(return_value=[test_feed_good])
        result = PFSImp.get_all_posts_service(test_feed_good.user_id)
        assert result[0]['user_id'] == -1
    except postIdNonExistent as e:
        assert str(e) == 'Id not found, please try again'


def test_service_delete_a_post():
    try:
        PFSImp.post_feed_dao.delete_a_post = MagicMock(
            return_value=[Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")])
        PFSImp.delete_a_post_service(test_feed_good)
        assert False
    except postIdNonExistent as e:
        assert str(e) == "Id not found, please try again."


def test_service_get_all_posts_with_user_id():


def get_all_posts(self)
    result =


# team_service.team_dao.get_all_teams_information = MagicMock(
#     return_value=[Team(21, "Pistons", "something else")])

# def service_get_team_information_by_id(self, team_id: str) -> Team:
#     try:
#         id_as_int = int(team_id)
#         return self.team_dao.get_team_information_by_id(id_as_int)
#         # return self.team_dao.get_team_information_by_id(int(team_id))
#     except ValueError:
#         raise BadTeamInfo("Please provide a valid team Id")