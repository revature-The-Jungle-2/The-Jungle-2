from custom_exceptions.post_image_not_found import PostImageNotFound
from custom_exceptions.post_not_found import PostNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.abstract_classes.create_post_dao_abs import CreatePostDAO
from entities.post import Post
from util.database_connection import connection


class CreatePostDAOImp(CreatePostDAO):

    def create_post(self, post: Post) -> Post:
        """a method to create a post in the database"""
        # Check to see if the user id is in the database, raise an error otherwise.
        sql = "select * from user_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": post.user_id})
        if not cursor.fetchone():
            raise UserNotFound('The user could not be found.')

        # Create the post.
        sql = "insert into post_table values(default, %s, NULL, %s, %s, 0, default) returning post_id"
        cursor = connection.cursor()
        cursor.execute(sql, (post.user_id, post.post_text, post.image_format))
        connection.commit()
        returned_post_id = cursor.fetchone()[0]

        # get the image from the database and send it back
        cursor = connection.cursor()
        sql = f"select * from post_table where post_id = %(post_id)s;"
        cursor.execute(sql, {"post_id": returned_post_id})
        connection.commit()
        new_post = cursor.fetchone()
        return Post(*new_post)

    def create_post_image(self, post_id: int, image: str) -> str:
        """a method to place a post image into the database"""
        # Check to see if the post id is in the database, raise an error otherwise.
        sql = f"select * from post_table where post_id = %(post_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id})
        if not cursor.fetchone():
            raise PostNotFound('The post could not be found.')

        # Make certain there is no other image
        sql = f"delete from post_picture_table where post_id = %(post_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id})
        connection.commit()

        # insert the image into the database
        sql = f"INSERT INTO post_picture_table VALUES (default, %(post_id)s, %(image)s)"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id, "image": image})
        connection.commit()

        # get the new image from the database and send it back
        sql = f"select picture from post_picture_table where post_id = %(post_id)s;"
        cursor.execute(sql, {"post_id": post_id})
        connection.commit()
        image = cursor.fetchone()[0]
        image_decoded = image.decode('utf-8')
        return image_decoded

    def get_post_image(self, post_id: int) -> str:
        """a method to get a post image from the database."""
        # Check to see if the post id is in the database, raise an error otherwise.
        sql = f"select * from post_picture_table where post_id = %(post_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"post_id": post_id})
        if not cursor.fetchone():
            raise PostImageNotFound('The post image could not be found.')

        # get the image from the database and send it back
        cursor = connection.cursor()
        sql = f"select picture from post_picture_table where post_id = %(post_id)s;"
        cursor.execute(sql, {"post_id": post_id})
        connection.commit()
        image = cursor.fetchone()[0]
        image_decoded = image.decode('utf-8')
        return image_decoded
