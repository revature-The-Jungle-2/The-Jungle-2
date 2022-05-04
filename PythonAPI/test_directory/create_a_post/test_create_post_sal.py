from custom_exceptions.post_not_found import PostNotFound
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from entities.post import Post
from service_layer.implementation_classes.create_post_service import CreatePostServiceImp

create_post_dao = CreatePostDAOImp()
create_post_service_abs = CreatePostServiceImp(create_post_dao)


# Mock Success
# Mock Fail
# Negative Test PostIdMustBeInteger
# Negative test PostTextMustBeString


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


def test_post_id_must_be_integer():
    try:
        post = Post("string", 2, 3, "text", "image format", 4, "date of post")
        result_post = create_post_dao.create_post(post)
        assert False
    except PostNotFound as e:
        assert str(e) == "Invalid information entered"


def test_post_text_must_be_string():
    try:
        post = Post(1, 2, 3, 444, "image format", 4, "date of post")
        result_post = create_post_dao.create_post(post)
        assert False
    except PostNotFound as e:
        assert str(e) == "Invalid information entered"


def test_post_group_id_not_found():
    try:
        post = Post(1, 2, 34567891011, "text", "image format", 4, "date of post")
        result_post = create_post_dao.create_post(post)
        assert False
    except PostNotFound as e:
        assert str(e) == "Invalid information entered Group Id not found"
