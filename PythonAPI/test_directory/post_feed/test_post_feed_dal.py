from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
from entities.post import Post

PFImp = PostFeedDaoImp()

test_feed = Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")


def test_get_all_posts():
    posts = PFImp.get_all_posts()
    assert len(posts) >= 2


# def test_get_all_posts_not_found():

def test_delete_a_post():
    delete = Post()
    result = PFImp.delete_a_post(delete.post_id)
    assert result == True


# def test_delete_a_post_post_not_found():

def test_get_all_posts_with_user_id():
    result = PFImp.get_all_posts_with_user_id(test_feed.user_id)
    assert result.__sizeof__() >= 1

# def test_get_all_post_with_user_id_not_found():
