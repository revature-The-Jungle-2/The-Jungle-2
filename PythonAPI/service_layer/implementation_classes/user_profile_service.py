from custom_exceptions.birth_date_is_null import BirthDateIsNull
from custom_exceptions.image_format_must_be_a_string import ImageFormatMustBeAString
from custom_exceptions.image_must_be_a_string import ImageMustBeAString
from custom_exceptions.too_many_characters import TooManyCharacters
from custom_exceptions.user_id_must_be_an_integer import UserIdMustBeAnInteger
from data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp
from entities.user import User
from service_layer.abstract_classes.user_profile_service_abs import UserProfileService


class UserProfileServiceImp(UserProfileService):
    def __init__(self, user_profile_dao):
        self.user_profile_dao: UserProfileDAOImp = user_profile_dao

    def service_get_user_profile_service(self, user_id: int) -> User:
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')
        return self.user_profile_dao.get_user_profile(user_id)

    def update_user_profile_service(self, user: User) -> User:
        """ Checks if the birthdate is null, and if the about me is too long"""

        if user.user_birth_date:
            if len(user.user_about) < 500:
                return self.user_profile_dao.update_user_profile(user)
            else:
                raise TooManyCharacters("Too many characters.")
        else:
            raise BirthDateIsNull("Birthdate cannot be null.")

    def get_user_image_service(self, user_id: int) -> str:
        # Check to make sure the user_id is an integer
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')

        return self.user_profile_dao.get_user_image(user_id)

    def update_user_image_service(self, user_id: int, image: str) -> str:
        # Check to make sure the user_id is an integer
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')

        # Check to make sure that the image is a string
        if not type(image) == str or not image:
            raise ImageMustBeAString("The image must be a string format.")

        return self.user_profile_dao.update_user_image(user_id, image)

    def update_user_image_format_service(self, user_id: int, image_format: str) -> User:
        """Service layer method to check user_id and image_date then send to data access layer."""
        # Check to make sure the user_id is an integer
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')

        # Check to make sure that the image format is a string
        if not type(image_format) == str or not image_format:
            raise ImageFormatMustBeAString('The image format must be a string.')

        return self.user_profile_dao.update_user_image_format(user_id, image_format)

    def update_password_service(self, user_id: int, password: str) -> User:
        """Stretch"""
        pass

    def get_user_followers_service(self, user_id: int) -> dict[str:int]:
        """Stretch"""
        # Check to make sure the user_id is an integer
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')
        return self.user_profile_dao.get_user_followers(user_id)

    def get_users_following_user_service(self, user_id: int) -> dict[str:int]:
        """Stretch"""
        # Check to make sure the user_id is an integer
        if not str(user_id).isnumeric():
            raise UserIdMustBeAnInteger('The user id must be an integer.')
        return self.user_profile_dao.get_users_following_user(user_id)

    def follow_user_service(self, user_follower_id: int, user_being_followed_id: int) -> bool:
        # Check to make sure the user_follower_id and user_being_followed_id is an integer
        if not (str(user_follower_id).isnumeric() and str(user_being_followed_id).isnumeric()):
            raise UserIdMustBeAnInteger('The user id must be an integer.')
        return self.user_profile_dao.follow_user(user_follower_id, user_being_followed_id)

    def unfollow_user_service(self, user_follower_id: int, user_being_followed_id: int) -> bool:
        # Check to make sure the user_follower_id and user_being_followed_id is an integer
        if not (str(user_follower_id).isnumeric() and str(user_being_followed_id).isnumeric()):
            raise UserIdMustBeAnInteger('The user id must be an integer.')
        return self.user_profile_dao.unfollow_user(user_follower_id, user_being_followed_id)
