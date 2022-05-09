from custom_exceptions.image_format_must_be_a_string import ImageFormatMustBeAString
from custom_exceptions.post_not_found import PostNotFound
from custom_exceptions.post_text_must_be_a_string import PostTextMustBeAString
from custom_exceptions.user_id_must_be_an_integer import UserIdMustBeAnInteger
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from entities.post import Post
from service_layer.implementation_classes.create_post_service import CreatePostServiceImp
from unittest.mock import MagicMock, patch

post_dao = CreatePostDAOImp()
post_service = CreatePostServiceImp(post_dao)
post = Post(1, 4, 3, "text", "image format", 4, "date of post")


@patch("data_access_layer.implementation_classes.create_post_dao.CreatePostDAOImp.create_post")
def test_create_post_service_mock_failure(mock):
    mock.side_effect = PostNotFound("The post could not be found.")
    try:
        result = post_service.create_post_service(post)
        assert False
    except PostNotFound as e:
        assert str(e) == "The post could not be found."


def test_create_post_service_mock_success():
    post_service.create_post_dao.create_post = MagicMock(return_value="http://placecorgi.com/260/180")
    result = post_service.create_post_service(post)
    assert result == "http://placecorgi.com/260/180"


def test_create_post_service_user_id_must_be_integer():
    try:
        result = post_service.create_post_service(Post(1, "a", 3, "text", "image format", 4, "date of post")
                                                  )
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == "The user id must be an integer."


def test_create_post_service_post_text_must_be_string():
    try:
        result = post_service.create_post_service(Post(1, 4, 3, 9876, "image format", 4, "date of post")
                                                  )
        assert False
    except PostTextMustBeAString as e:
        assert str(e) == "The post text must be a string."


def test_create_post_service_image_format_must_be_string():
    try:
        result = post_service.create_post_service(Post(1, 4, 3, "text", 44, 4, "date of post")
                                                  )
        assert False
    except ImageFormatMustBeAString as e:
        assert str(e) == "The image format must be a string."
