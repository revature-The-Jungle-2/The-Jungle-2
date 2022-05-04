from custom_exceptions.follower_not_found import FollowerNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp

user_profile_dao = UserProfileDAOImp()


def test_dao_update_password_success():
    pass


def test_dao_get_user_followers_success():  # CHECK DATABASE AND REFACTOR
    followers = user_profile_dao.get_user_followers(1)
    assert len(followers) >= 1


def test_dao_get_user_followers_id_not_found():
    try:
        user_profile_dao.get_user_followers(-59595)
        assert False
    except UserNotFound as e:
        assert str(e) == 'The user could not be found.'


def test_dao_get_users_following_user_success():  # CHECK DATABASE AND REFACTOR ALSO STRETCH
    users_following = user_profile_dao.get_users_following_user(3)
    assert len(users_following) >= 1


def test_dao_get_users_following_user_user_id_not_found():
    try:
        user_profile_dao.get_users_following_user(-59595)
        assert False
    except UserNotFound as e:
        assert str(e) == 'The user could not be found.'


def test_dao_follow_user_success(): # CHECK DATABASE AND REFACTOR FROM HERE UNTIL BOTTOM FOR ID #s
    result = user_profile_dao.follow_user(1, 2)
    assert result is True


def test_dao_follow_user_user_follower_id_not_found():
    try:
        user_profile_dao.follow_user(-59595, 1)
        assert False
    except UserNotFound as e:
        assert str(e) == 'The user could not be found.'


def test_dao_follow_user_user_being_followed_id_not_found():
    try:
        user_profile_dao.follow_user(1, -59595)
        assert False
    except UserNotFound as e:
        assert str(e) == 'The user could not be found.'


def test_dao_unfollow_user_success():
    result = user_profile_dao.unfollow_user(2, 1)
    assert result is True


def test_dao_unfollow_user_user_follower_id_not_found():
    try:
        user_profile_dao.unfollow_user(-132093, 1)
        assert False
    except FollowerNotFound as e:
        assert str(e) == "The follower was not found."


def test_dao_unfollow_user_user_being_followed_id_not_found():
    try:
        user_profile_dao.unfollow_user(1, -59595)
        assert False
    except FollowerNotFound as e:
        assert str(e) == 'The follower was not found.'

