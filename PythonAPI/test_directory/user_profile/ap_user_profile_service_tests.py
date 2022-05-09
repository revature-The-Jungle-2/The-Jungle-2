from unittest.mock import MagicMock
from custom_exceptions.user_id_must_be_an_integer import UserIdMustBeAnInteger
from data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp
from service_layer.implementation_classes.user_profile_service import UserProfileServiceImp

user_profile_dao = UserProfileDAOImp()
user_profile_service = UserProfileServiceImp(user_profile_dao)


def test_service_update_password_success():
    pass


def test_service_get_user_followers_success():  #STUBBED
    user_profile_service.user_profile_dao.get_user_followers = MagicMock(return_value={'matty': 4})
    followers = user_profile_service.get_user_followers_service(4)
    print(followers)
    assert len(followers) >= 1


def test_service_get_user_followers_user_id_numeric():
    try:
        user_profile_service.get_user_followers_service("words")
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'


def test_service_get_users_following_user_success():  #STUBBED
    user_profile_service.user_profile_dao.get_users_following_user = MagicMock(return_value={'LunaBear9197': 5})
    users_following = user_profile_service.get_users_following_user_service(5)
    print(users_following)
    assert len(users_following) >= 1


def test_service_get_users_following_user_user_id_numeric():
    try:
        user_profile_service.get_users_following_user_service("more words")
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'


def test_service_follow_user_success():  #STUBBED
    user_profile_service.user_profile_dao.follow_user = MagicMock(return_value=True)
    result = user_profile_service.follow_user_service(4, 6)
    assert result is True


def test_service_follow_user_user_follower_id_numeric():
    try:
        user_profile_service.follow_user_service("words", 6)
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'


def test_service_follow_user_user_being_followed_id_numeric():
    try:
        user_profile_service.follow_user_service(4, "words")
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'


def test_service_unfollow_user_success():  #STUBBED
    user_profile_service.user_profile_dao.unfollow_user = MagicMock(return_value=True)
    result = user_profile_service.unfollow_user_service(4, 6)
    assert result is True


def test_service_unfollow_user_user_follower_id_numeric():
    try:
        user_profile_service.unfollow_user_service("words", 6)
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'


def test_service_unfollow_user_user_being_followed_id_numeric():
    try:
        user_profile_service.unfollow_user_service(4, "-words")
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'

