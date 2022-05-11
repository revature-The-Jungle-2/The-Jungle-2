
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAOAbs
from entities.group_post import GroupPost
from util.database_connection import connection



# From Test Post Feed as example:

# from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
# from entities.post import Post
#
# PFImp = PostFeedDaoImp()
#
# test_feed = Post(1, 1, 1, "My cat", "jpeg", 1, "Tuesday, January 1 2020, 13:24:56")



# From Group Post DAO IMP:
# from typing import List
#
# from custom_exceptions.post_exceptions import PostNotFound
# from data_access_layer.abstract_classes.group_post_dao_abs import GroupPostDAOAbs
# from entities.group_post import GroupPost
# from util.database_connection import connection
#
# schema_prefix = "p3."
#
# class GroupPostDAO(GroupPostDAOAbs):


# From Post Feed DAO Imp as example:
# from typing import List
#
# from custom_exceptions.connection_error import ConnectionErrorr
# from data_access_layer.abstract_classes.postfeed_dao_abs import PostFeedDao
# from entities.post import Post
# from util.database_connection import connection
#
# schema_prefix = "p3."
#
#
# class PostFeedDaoImp(PostFeedDao):