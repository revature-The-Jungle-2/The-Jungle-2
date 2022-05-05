from custom_exceptions.post_id_must_be_an_integer import PostIdMustBeAnInteger
from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from service_layer.implementation_classes.create_post_service import CreatePostServiceImp
from unittest.mock import MagicMock, patch

post_dao = CreatePostDAOImp()
post_service = CreatePostServiceImp(post_dao)


@patch("data_access_layer.implementation_classes.create_post_dao.CreatePostDAOImp.create_post_image")
def test_create_post_service_mock_failure(mock):
    mock.side_effect = PostNotFound("The post could not be found.")
    try:
        result = post_service.create_post_service(9, 123456789)
        assert False
    except PostNotFound as e:
        assert str(e) == "The post could not be found."


def test_create_post_service_mock_success():
    post_service.create_post_dao.create_post = MagicMock(return_value="http://placecorgi.com/260/180")
    result = post_service.create_post_service(9, 123456789)
    assert result == "http://placecorgi.com/260/180"


def test_create_post_service_post_id_must_be_integer():
    try:
        result = post_service.create_post_service("xyz", "http://placecorgi.com/260/180")
        assert False
    except PostIdMustBeAnInteger as e:
        assert str(e) == "The post id must be an integer."


def test_create_post_service_post_text_must_be_string():
    try:
        result = post_service.create_post_service(1, 2)
        assert False
    except PostNotFound as e:
        assert str(e) == "The post text must be a string."



