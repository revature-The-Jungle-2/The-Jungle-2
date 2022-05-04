from custom_exceptions.post_image_not_found import PostImageNotFound
from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp

post_dao = CreatePostDAOImp()


# Create post image function
def test_create_post_image_success():
    result = post_dao.create_post_image(2, "http://placecorgi.com/260/180")
    assert result == "http://placecorgi.com/260/180"


def test_create_post_image_post_not_found():
    try:
        result = post_dao.create_post_image(324534, "http://placecorgi.com/260/180")
    except PostNotFound as e:
        assert str(e) == "The post could not be found."


# Get post image
def test_get_post_image_success():
    result = post_dao.get_post_image(2)
    assert result == "http://placecorgi.com/260/180"


def test_get_post_image_post_image_not_found():
    try:
        result = post_dao.get_post_image(234234234)
    except PostImageNotFound as e:
        assert str(e) == "The post image could not be found."
