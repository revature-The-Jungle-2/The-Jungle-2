from custom_exceptions.follower_not_found import FollowerNotFound
from custom_exceptions.user_image_not_found import UserImageNotFound
from custom_exceptions.user_not_found import UserNotFound
from data_access_layer.abstract_classes.user_profile_dao_abs import UserProfileDAO
from entities.user import User
from util.database_connection import connection

user_not_found_string = 'The user could not be found.'


class UserProfileDAOImp(UserProfileDAO):

    def get_user_profile(self, user_id: int) -> User:
        """Grabs data from the user profile by user id"""
        sql = 'select * from user_table where user_id = %(user_id)s'
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        profile_record = cursor.fetchone()
        if profile_record:
            user = User(*profile_record)
            return user
        else:
            raise UserNotFound(user_not_found_string)

    def update_user_profile(self, user: User) -> User:
        """ A method used to update information for the profile besides the image"""

        sql = "select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {'user_id': user.user_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        sql = "update user_table set user_about = %(user_about)s, user_birth_date = %(user_birth_date)s where user_id " \
              "= %(user_id)s "
        cursor.execute(sql, {'user_about': user.user_about, 'user_birth_date': user.user_birth_date,
                             'user_id': user.user_id})

        sql = "select * from user_table where user_id = %(user_id)s"
        cursor.execute(sql, {"user_id": user.user_id})

        connection.commit()
        return user

    def get_user_image(self, user_id: int) -> str:
        """a method to get a user image from the database"""  # need to create a custom exception and database checker

        # Check to see if the post id is in the database, raise an error otherwise.
        sql = f"select user_id from user_picture_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        if not cursor.fetchone():
            raise UserImageNotFound('The user image could not be found.')

        sql = "select picture from user_picture_table where user_id = %(user_id)s;"
        cursor.execute(sql, {"user_id": user_id})
        image = cursor.fetchone()[0]
        image_decoded = image.decode('utf-8')
        return image_decoded

    def update_user_image(self, user_id: int, image: str) -> str:
        """a method to place a user image into the database"""

        # Check to see if the user id is in the database, raise an error otherwise.
        sql = "select * from user_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        # delete any existing image from the database and place the image in the database
        sql = "DELETE FROM user_picture_table where user_id = %(user_id)s; "
        cursor.execute(sql, {"user_id": user_id})
        connection.commit()

        # do the thing
        sql = "INSERT INTO user_picture_table VALUES (default, %(user_id)s, %(image)s);"
        cursor.execute(sql, {"user_id": user_id, "image": image})
        connection.commit()

        # get the new image and send it back up to the service layer
        sql = f"select picture from user_picture_table where user_id = %(user_id)s;"
        cursor.execute(sql, {"user_id": user_id})
        connection.commit()
        image = cursor.fetchone()[0]
        image_decoded = image.decode('utf-8')
        return image_decoded

    def update_user_image_format(self, user_id: int, image_format: str) -> User:
        """Method to put the picture format into the database."""

        # Check to see if the user id is in the database, raise an error otherwise.
        sql = f"select * from user_table where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        # Update the user image format.
        sql = f"update user_table set image_format = %(image_format)s where user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"image_format": image_format, "user_id": user_id})
        connection.commit()

        # Grab the user from the database and send it back.
        sql = f"select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        connection.commit()
        profile_record = cursor.fetchone()
        user = User(*profile_record)
        return user

    def update_password(self, user_id: int, password: str) -> User:
        """Stretch"""
        pass

    def get_user_followers(self, user_id: int) -> dict[str:int]:
        """Returns a dictionary with username as key and their userId as the value of the followers of userID"""
        sql = "select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {'user_id': user_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        sql = "select user_table.username, user_follower_id from user_follow_junction_table" \
              " inner join user_table on user_follow_junction_table.user_follower_id = user_table.user_id" \
              " where user_follow_junction_table.user_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        connection.commit()
        follower_records = cursor.fetchall()
        follower_dict = {}
        for follower in follower_records:
            follower_dict.update({follower[0]: follower[1]})
        return follower_dict

    def get_users_following_user(self, user_id: int) -> dict[str:int]:
        """Stretch"""
        sql = "select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {'user_id': user_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        sql = "select user_table.username, user_table.user_id from user_follow_junction_table" \
              " inner join user_table on user_follow_junction_table.user_id = user_table.user_id" \
              " where user_follower_id = %(user_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_id})
        connection.commit()
        following_records = cursor.fetchall()
        following_dict = {}
        for follower in following_records:
            following_dict.update({follower[0]: follower[1]})
        return following_dict

    def follow_user(self, user_follower_id: int, user_being_followed_id: int) -> bool:

        sql = "select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_follower_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        sql = "select * from user_table where user_id = %(user_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_id": user_being_followed_id})
        if not cursor.fetchone():
            raise UserNotFound(user_not_found_string)

        sql = "insert into user_follow_junction_table values(%(user_follower_id)s, %(user_being_followed_id)s, false)"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_follower_id": user_follower_id, "user_being_followed_id": user_being_followed_id})
        connection.commit()
        return True

    def unfollow_user(self, user_follower_id: int, user_being_followed_id: int) -> bool:
        sql = "select * from user_follow_junction_table where user_follower_id = %(user_follower_id)s" \
              " and user_id = %(user_being_followed_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {'user_follower_id': user_follower_id, "user_being_followed_id": user_being_followed_id})
        if not cursor.fetchone():
            raise FollowerNotFound("The follower was not found.")

        sql = "delete from user_follow_junction_table where user_follower_id = %(user_follower_id)s" \
              " and user_id = %(user_being_followed_id)s"
        cursor = connection.cursor()
        cursor.execute(sql, {"user_follower_id": user_follower_id, "user_being_followed_id": user_being_followed_id})
        connection.commit()
        return True

