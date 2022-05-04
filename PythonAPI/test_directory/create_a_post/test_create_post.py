from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from entities.post import Post


create_post_dao = CreatePostDAOImp()


def test_create_post_success():
    post = Post(1, 2, 3, "text", "image format", 4, "date of post")
    result_post = create_post_dao.create_post(post)
    assert result_post.post_id != 0


def test_create_post_failure():
    try:
        post = Post(1, 123456789, 3, "text", "image format", 4, "date of post")
        result_post = create_post_dao.create_post(post)
        assert False
    except PostNotFound as e:
        assert str(e) == "Invalid information entered"
