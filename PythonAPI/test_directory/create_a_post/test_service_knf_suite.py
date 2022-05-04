from unittest.mock import MagicMock, patch

from custom_exceptions.image_must_be_a_string import ImageMustBeAString
from custom_exceptions.post_id_must_be_an_integer import PostIdMustBeAnInteger
from custom_exceptions.post_image_not_found import PostImageNotFound
from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from service_layer.implementation_classes.create_post_service import CreatePostServiceImp

post_dao = CreatePostDAOImp()
post_service = CreatePostServiceImp(post_dao)


# Create Post Image
@patch("data_access_layer.implementation_classes.create_post_dao.CreatePostDAOImp.create_post_image")
def test_create_post_image_service_mock_failure(mock):
    mock.side_effect = PostNotFound("The post could not be found.")
    try:
        result = post_service.create_post_image_service(2, "bananas")
        assert False
    except PostNotFound as e:
        assert str(e) == "The post could not be found."


def test_create_post_image_service_mock_success():
    post_service.create_post_dao.create_post_image = MagicMock(return_value="http://placecorgi.com/260/180")
    result = post_service.create_post_image_service(2, "bananas")
    assert result == "http://placecorgi.com/260/180"


def test_create_post_image_service_negative_post_id_integer():
    try:
        result = post_service.create_post_image_service("a", "http://placecorgi.com/260/180")
        assert False
    except PostIdMustBeAnInteger as e:
        assert str(e) == "The post id must be an integer."


def test_create_post_image_service_image_must_be_string():
    try:
        result = post_service.create_post_image_service(2, 4)
        assert False
    except ImageMustBeAString as e:
        assert str(e) == "The image must be a string format."


# Get post image
@patch("data_access_layer.implementation_classes.create_post_dao.CreatePostDAOImp.get_post_image")
def test_get_post_image_service_mock_failure(mock):
    mock.side_effect = PostImageNotFound("The post image could not be found.")
    try:
        result = post_service.get_post_image_service(4)
        assert False
    except PostImageNotFound as e:
        assert str(e) == "The post image could not be found."


def test_get_post_image_service_mock_success():
    post_service.create_post_dao.get_post_image = MagicMock(return_value="bananas")
    result = post_service.get_post_image_service(3)
    assert result == "bananas"


def test_get_post_image_service_negative_post_id_integer():
    try:
        result = post_service.get_post_image_service("a")
        assert False
    except PostIdMustBeAnInteger as e:
        assert str(e) == "The post id must be an integer."
