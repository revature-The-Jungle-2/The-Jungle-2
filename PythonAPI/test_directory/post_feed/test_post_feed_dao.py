from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
from entities.post import Post

PFImp = PostFeedDaoImp()

test_feed = Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")


def test_get_all_posts():
    posts = PFImp.get_all_posts()
    assert len(posts) >= 2

def test_delete_a_post():
    result = PFImp.delete_a_post(test_feed.post_id)
    assert result != 1


def test_get_all_posts_with_user_id():
    result = PFImp.get_all_posts_with_user_id(test_feed.user_id)
    assert result == 1


