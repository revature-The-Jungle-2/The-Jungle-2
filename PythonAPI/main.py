import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

from custom_exceptions.birth_date_is_null import BirthDateIsNull
from custom_exceptions.connection_error import ConnectionErrorr
from custom_exceptions.follower_not_found import FollowerNotFound
from custom_exceptions.group_exceptions import NullValues, InputTooShort, InputTooLong, GroupNameTaken
from custom_exceptions.group_member_junction_exceptions import WrongId
from custom_exceptions.image_format_must_be_a_string import ImageFormatMustBeAString
from custom_exceptions.image_must_be_a_string import ImageMustBeAString
from custom_exceptions.post_exceptions import InvalidInput
from custom_exceptions.post_id_must_be_an_integer import PostIdMustBeAnInteger
from custom_exceptions.post_image_not_found import PostImageNotFound
from custom_exceptions.post_not_found import PostNotFound
from custom_exceptions.post_text_must_be_a_string import PostTextMustBeAString
from custom_exceptions.too_many_characters import TooManyCharacters
from custom_exceptions.user_id_must_be_an_integer import UserIdMustBeAnInteger
from custom_exceptions.user_image_not_found import UserImageNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.implementation_classes.comment_dao import CommentDAOImp
from data_access_layer.implementation_classes.create_post_dao import CreatePostDAOImp
from data_access_layer.implementation_classes.group_dao import GroupDAOImp
from data_access_layer.implementation_classes.group_member_junction_dao import GroupMemberJunctionDao
from data_access_layer.implementation_classes.group_post_dao import GroupPostDAO
from data_access_layer.implementation_classes.group_view_postgres_dao import GroupViewPostgresDao
from data_access_layer.implementation_classes.like_post_dao import LikePostDaoImp
from data_access_layer.implementation_classes.postfeed_dao import PostFeedDaoImp
from data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp
from entities.group import Group
from entities.group_post import GroupPost
from entities.post import Post
from entities.user import User
from service_layer.implementation_classes.comment_service import CommentServiceImp
from service_layer.implementation_classes.create_post_service import CreatePostServiceImp
from service_layer.implementation_classes.group_member_junction_service import GroupMemberJunctionService
from service_layer.implementation_classes.group_post_service import GroupPostService
from service_layer.implementation_classes.group_postgres_service import GroupPostgresService
from service_layer.implementation_classes.group_service import GroupPostgreService
from service_layer.implementation_classes.like_post_service import LikePostServiceImp
from service_layer.implementation_classes.postfeed_service import PostFeedServiceImp
from service_layer.implementation_classes.user_profile_service import UserProfileServiceImp

logging.basicConfig(filename="records.log", level=logging.DEBUG,
                    format="[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")

# Setup flask
app: Flask = Flask(__name__)
CORS(app)

@app.get("/")  # basic check for app running
def on():
    return "python is running"


create_post_dao = CreatePostDAOImp()
create_post_service = CreatePostServiceImp(create_post_dao)
user_profile_dao = UserProfileDAOImp()
user_profile_service = UserProfileServiceImp(user_profile_dao)
group_view_dao = GroupViewPostgresDao()
group_service = GroupPostgresService(group_view_dao)
group_post_dao = GroupPostDAO()
group_post_service = GroupPostService(group_post_dao)
post_feed_dao = PostFeedDaoImp()
post_feed_service = PostFeedServiceImp(post_feed_dao)
comment_dao = CommentDAOImp()
comment_service = CommentServiceImp(comment_dao)
group_dao = GroupDAOImp()
group_service2 = GroupPostgreService(group_dao, group_view_dao)  # Possibly need to clean up the code.
like_post_dao = LikePostDaoImp()
like_post_service = LikePostServiceImp(like_post_dao)


@app.get("/user/<user_id>")
def get_a_user_id(user_id: int):
    try:
        user = user_profile_service.service_get_user_profile_service(int(user_id))
        user_as_dictionary = user.make_dictionary()
        return jsonify(user_as_dictionary), 200
    except UserNotFound as e:
        return str(e), 400


@app.post("/post")
def create_a_post():  # Not yet tested
    """Method to create a new post in the database."""
    post_body = request.get_json()
    new_post = Post(user_id=post_body["user_id"],
                    post_text=post_body["post_text"],
                    image_format=post_body["image_format"])
    try:
        returned_post = create_post_service.create_post_service(new_post)
        returned_post_as_json = jsonify(returned_post.make_dictionary())
        return returned_post_as_json
    except UserIdMustBeAnInteger as e:
        return str(e), 400
    except ImageFormatMustBeAString as e:
        return str(e), 400
    except PostTextMustBeAString as e:
        return str(e), 400
    except UserNotFound as e:
        return str(e), 400


@app.post("/post/image/<post_id>")
def create_a_post_image(post_id):
    """Method to insert an image into the database. Returns the same image back from the database."""
    try:
        image = request.data
        image_decoded = image.decode('utf-8')
        return create_post_service.create_post_image_service(post_id, image_decoded), 201
    except PostIdMustBeAnInteger as e:
        return str(e), 400
    except ImageMustBeAString as e:
        return str(e), 400
    except PostNotFound as e:
        return str(e), 400


@app.get("/post/image/<post_id>")
def get_the_post_image(post_id):
    """Method to grab the post image from the database by the post id."""
    try:
        return create_post_service.get_post_image_service(post_id), 200
    except PostIdMustBeAnInteger as e:
        return str(e), 400
    except PostImageNotFound as e:
        return str(e), 400


@app.get("/user/image/<user_id>")
def get_the_user_image(user_id):
    """Method to grab a user image from the database by the user id."""
    try:
        return user_profile_service.get_user_image_service(user_id), 200
    except UserIdMustBeAnInteger as e:
        return str(e), 400
    except UserImageNotFound as e:
        return str(e), 400


@app.post("/user/image/<user_id>")
def post_the_user_image(user_id):
    try:
        image = request.data
        image_decoded = image.decode('utf-8')
        return user_profile_service.update_user_image_service(user_id, image_decoded), 200
    except UserIdMustBeAnInteger as e:
        return str(e), 400
    except ImageMustBeAString as e:
        return str(e), 400
    except UserNotFound as e:
        return str(e), 400


@app.post("/user/imageFormat/<user_id>")
def post_the_user_image_format(user_id):
    try:
        image_data = request.get_json()
        returned_user = user_profile_service.update_user_image_format_service(user_id, image_data["image_format"])
        user_as_json = jsonify(returned_user.make_dictionary())
        return user_as_json, 200
    except UserIdMustBeAnInteger as e:
        return str(e), 400
    except ImageFormatMustBeAString as e:
        return str(e), 400
    except UserNotFound as e:
        return str(e), 400


@app.patch("/user/profile/update/<user_id>")
def update_profile_info(user_id):
    try:
        user_profile_data = request.get_json()
        new_user_profile = User(
            user_id,
            user_profile_data["firstName"],
            user_profile_data["lastName"],
            user_profile_data["email"],
            user_profile_data["username"],
            user_profile_data["passcode"],
            user_profile_data["userAbout"],
            user_profile_data["userBirthDate"],
            user_profile_data["userImageFormat"]
        )
        returned_user_profile = user_profile_service.update_user_profile_service(
            new_user_profile)
        user_profile_as_dictionary = returned_user_profile.make_dictionary()
        user_profile_as_json = jsonify(user_profile_as_dictionary)
        return user_profile_as_json, 200
    except UserNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except TooManyCharacters as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except BirthDateIsNull as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# -----------------------------------------------------------------------------------------------------

# CREATE GROUP
@app.post("/group")
def create_group():
    try:
        group_data = request.get_json()
        new_group = Group(
            group_data["groupId"],
            int(group_data["userId"]),
            group_data["groupName"],
            group_data["groupAbout"],
            group_data["imageFormat"]
        )
        group_created: Group = group_service2.service_create_group(new_group)
        group_dictionary = group_created.make_dictionary()
        group_json = jsonify(group_dictionary)
        return group_json, 201
    except NullValues as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400
    except InputTooShort as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400
    except InputTooLong as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400
    except GroupNameTaken as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400


# JOIN GROUP
@app.post("/group/join/<group_id>/<user_id>")
def join_group(group_id: str, user_id: str):
    group_joined = group_service2.service_join_group(int(group_id), int(user_id))
    group_joined_dictionary = {
        "groupId": group_joined[0],
        "userId": group_joined[1]
    }
    return jsonify(group_joined_dictionary), 200


# -----------------------------------------------------------------------------------------------------


@app.get("/group/<group_id>")
def get_group_by_id(group_id: str):
    group = group_service.service_get_group_by_id(int(group_id))
    group_as_dictionary = group.make_dictionary()
    group_as_json = jsonify(group_as_dictionary)
    return group_as_json


@app.get("/group")
def get_all_groups():
    groups_as_groups = group_service.service_get_all_groups()
    groups_as_dictionary = []
    for groups in groups_as_groups:
        dictionary_group = groups.make_dictionary()
        groups_as_dictionary.append(dictionary_group)
    return jsonify(groups_as_dictionary)


@app.get("/group/user/<user_id>")
def get_all_groups_by_user_id(user_id: str):
    groups_as_groups = group_service.service_get_groups_by_user_id(int(user_id))
    groups_as_dictionary = []
    for groups in groups_as_groups:
        dictionary_group = groups.make_dictionary()
        groups_as_dictionary.append(dictionary_group)
    return jsonify(groups_as_dictionary)


"""Group Junction API"""
group_mem_dao = GroupMemberJunctionDao()
group_junction_service = GroupMemberJunctionService(group_mem_dao)


@app.get("/GroupJunction/UserList/<group_id>")
def get_users_in_group_api(group_id):
    group_list = group_junction_service.get_all_users_in_a_group(int(group_id))
    group_dict = []
    for mem in group_list:
        dictionary_mem = mem.make_dictionary()
        group_dict.append(dictionary_mem)
    return jsonify(group_dict), 200


@app.delete("/group/leave/<user_id>/<group_id>")
def leave_group(user_id: str, group_id: str):
    try:
        group_junction_service.leave_group(int(user_id), int(group_id))
        message = "you have left the group"
        return jsonify(message), 200
    except TypeError as e:
        return jsonify(str(e)), 400
    except WrongId as e:
        return jsonify(str(e)), 400


@app.get("/user/post/<user_id>")
def get_all_user_posts(user_id):
    try:
        post_as_post = post_feed_service.get_all_posts_by_user_id_service(user_id)
        posts_as_dictionary = []
        for post in post_as_post:
            dictionary_posts = post.make_dictionary()
            posts_as_dictionary.append(dictionary_posts)
        return jsonify(posts_as_dictionary)
    except ConnectionErrorr as e:
        return str(e), 400


@app.get("/postfeed")
def get_all_posts():
    try:
        post_as_post = post_feed_service.get_all_posts_service()
        posts_as_dictionary = []
        for post in post_as_post:
            dictionary_posts = post.make_dictionary()
            posts_as_dictionary.append(dictionary_posts)
        return jsonify(posts_as_dictionary)
    except ConnectionErrorr as e:
        return str(e), 400


@app.delete("/postfeed")
def delete_a_post():
    try:
        data = request.get_json()
        postid = data["postId"]
        boolean = post_feed_service.delete_a_post_service(postid)
        return jsonify(boolean)
    except ConnectionErrorr as e:
        return str(e), 400


@app.post("/postfeed")
def add_likes_to_post():
    try:
        data = request.get_json()
        postid = data["postId"]
        return jsonify(like_post_service.service_like_post(postid))
    except TypeError:
        return ("post not found!"), 400


@app.post("/postfeed/comment")
def add_likes_to_comment():
    try:
        data = request.get_json()
        commentid = data["commentId"]
        return jsonify(like_post_service.service_like_comment(commentid))
    except TypeError:
        return ("comment not found"), 400


# delete comment information
@app.delete("/Comments")
def delete_comment():
    data = request.get_json()
    comment_id = data["commentId"]
    jsonify(comment_service.service_delete_comment(comment_id))
    return "Comment with id {} was deleted successfully".format(comment_id)


@app.get("/postfeed/<post_id>")
def get_comments_by_post_id(post_id: str):
    try:
        results = comment_service.service_get_comment_by_post_id(int(post_id))
        post_comments_as_dictionary = []
        for comments in results:
            dictionary_comment = comments.make_dictionary()
            post_comments_as_dictionary.append(dictionary_comment)
        return jsonify(post_comments_as_dictionary), 200
    except Exception:
        return "something went wrong"


@app.post("/createComment")
def create_comment():
    body = request.get_json()
    post_id = body["postId"]
    user_id = body["userId"]
    group_id = body["groupId"]
    reply_user = body["replyUser"]
    comment_text = body["commentText"]
    comment_id = comment_service.service_create_comment(post_id, user_id, comment_text, group_id, reply_user)
    return jsonify(comment_id)


"""Get Creator for Group HomePage"""


@app.get("/creator/<group_id>")
def get_creator_api(group_id: str):
    result = group_service2.service_get_creator(int(group_id))
    # dict = {
    #     "firstName": result.index(0),
    #     "lastName": result.index(1),
    #     "username": result.index(2)
    # }
    return jsonify(result), 200


# --------------------------------------------------------------------------------------------------------------------------------

@app.post("/group_post")
def create_group_post():
    try:
        post_data = request.get_json()
        new_post = GroupPost(
            0,
            int(post_data["user_id"]),
            int(post_data["group_id"]),
            post_data["post_text"],
            post_data["image_data"],
            int(post_data["likes"]),
            post_data["date_time_of_creation"]
        )
        post_to_return = group_post_service.service_create_post(new_post)
        post_as_dictionary = post_to_return.make_dictionary()
        post_as_json = jsonify(post_as_dictionary)
        return post_as_json, 201
    except InvalidInput as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.get("/group_post/<post_id>")
def get_group_post_by_id(post_id: str):
    result = group_post_service.service_get_post_by_id(int(post_id))
    dictionary_request = result.make_dictionary()
    return jsonify(dictionary_request), 200


@app.get("/group_post")
def get_all_group_posts():
    posts_as_posts = group_post_service.service_get_all_posts()
    posts_as_dictionary = []
    for posts in posts_as_posts:
        post_dictionary = posts.make_dictionary()
        posts_as_dictionary.append(post_dictionary)
    return jsonify(posts_as_dictionary), 200


@app.get("/group_post/group/<group_id>")
def get_all_group_posts_by_group_id(group_id: str):
    posts_as_posts = group_post_service.service_get_all_posts_by_group_id(int(group_id))
    posts_as_dictionary = []
    for posts in posts_as_posts:
        post_dictionary = posts.make_dictionary()
        posts_as_dictionary.append(post_dictionary)
    return jsonify(posts_as_dictionary), 200


@app.delete("/group_post/<post_id>")
def delete_group_post(post_id: int):
    result = group_post_service.service_delete_post_by_post_id(int(post_id))
    if result:
        return "Post with ID {} was deleted successfully".format(post_id)
    else:
        return "Something went wrong: Post with ID {} was not deleted".format(post_id)


@app.get("/user/followers/<user_id>")
def get_user_followers(user_id: int):
    try:
        followers = user_profile_service.get_user_followers_service(user_id)
        return jsonify(followers), 200
    except UserNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except UserIdMustBeAnInteger as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.get("/user/following/<user_id>")
def get_user_following(user_id: int):
    try:
        followers = user_profile_service.get_users_following_user_service(user_id)
        return jsonify(followers), 200
    except UserNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except UserIdMustBeAnInteger as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.post("/user/<user_follower_id>/followed/<user_being_followed_id>")
def follow_user(user_follower_id: int, user_being_followed_id: int):
    try:
        user_profile_service.follow_user_service(user_follower_id, user_being_followed_id)
        follow_dictionary = {"message": str(user_follower_id) + " has followed " + str(user_being_followed_id)}
        follow_json = jsonify(follow_dictionary)
        return follow_json, 200
    except UserIdMustBeAnInteger as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except FollowerNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except UserNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.post("/user/<user_follower_id>/unfollowed/<user_being_followed_id>")
def unfollow_user(user_follower_id: int, user_being_followed_id: int):
    try:
        user_profile_service.unfollow_user_service(user_follower_id, user_being_followed_id)
        unfollow_dictionary = {"message": str(user_follower_id) + " has unfollowed " + str(user_being_followed_id)}
        unfollow_json = jsonify(unfollow_dictionary)
        return unfollow_json, 200
    except UserIdMustBeAnInteger as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except FollowerNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except UserNotFound as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


app.run()
