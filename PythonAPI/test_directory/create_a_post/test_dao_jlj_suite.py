
from custom_exceptions.post_not_found import PostNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from entities.post import Post


create_post_dao = CreatePostDAOImp()


def test_create_post_success():
    post = Post(1, 4, 3, "text", "image format", 4, "date of post")
    result_post = create_post_dao.create_post(post)
    assert result_post.post_id != 0


def test_create_post_failure():
    try:
        post = Post(1, 123456789, 3, "text", "image format", 4, "date of post")
        result_post = create_post_dao.create_post(post)
        assert False
    except UserNotFound as e:
        assert str(e) == "The user could not be found."
