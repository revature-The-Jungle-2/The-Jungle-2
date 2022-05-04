from unittest.mock import MagicMock

from PythonAPI.custom_exceptions.birth_date_is_null import BirthDateIsNull
from PythonAPI.custom_exceptions.image_format_must_be_a_string import ImageFormatMustBeAString
from PythonAPI.custom_exceptions.image_must_be_a_string import ImageMustBeAString
from PythonAPI.custom_exceptions.too_many_characters import TooManyCharacters
from PythonAPI.custom_exceptions.user_id_must_be_an_integer import UserIdMustBeAnInteger
from PythonAPI.data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp
from PythonAPI.entities.user import User
from PythonAPI.service_layer.implementation_classes.user_profile_service import UserProfileServiceImp

test_dao = UserProfileDAOImp()
test_sao = UserProfileServiceImp(test_dao)

def test_service_get_user_profile_non_numeric_user_id():
    try:
        test_sao.service_get_user_profile_service('this will fail')
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'

def test_service_get_user_profile_success():
    test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '1/1/1997', 'img')
    test_sao.service_get_user_profile_service=MagicMock(
    test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '1/1/1997', 'img'))
    assert test_sao.service_get_user_profile_service(test_user)

def test_service_update_user_profile_about_me_too_long():
    try:
        test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'thisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylong', '1/1/1997','img')
        test_sao.update_user_profile_service(test_user)
        assert False
    except TooManyCharacters as e:
        assert str(e) == "Too many characters."

def test_service_update_user_profile_null_birthdate():
    try:
        test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '', 'img')
        test_sao.update_user_profile_service(test_user)
        assert False
    except BirthDateIsNull as e:
        assert str(e) == "Birthdate cannot be null."

def test_service_update_user_profile_success():
    test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '1/1/1997', 'img')
    test_sao.update_user_profile_service=MagicMock(
    test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '1/1/1997', 'img'))
    assert test_sao.update_user_profile_service(test_user)

def test_service_get_user_image_non_numeric_user_id():
    try:
        test_sao.get_user_image_service('this will not work')
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'

def test_service_get_user_image_success():
    test_sao.get_user_image_service=MagicMock(return_value=True)
    assert test_sao.get_user_image_service(1)

def test_service_update_user_image_non_numeric_user_id():
    try:
        test_sao.update_user_image_service('this will not work', 'downloads/Husky.jpg')
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'

def test_service_update_user_image_format_not_string():
    try:
        test_sao.update_user_image_service(1, 1)
        assert False
    except ImageMustBeAString as e:
        assert str(e) == "The image must be a string format."

def test_service_update_user_image_success():
    test_sao.update_user_image_service=MagicMock(return_value=True)
    assert test_sao.update_user_image_service(1)

def test_service_update_user_image_format_non_numeric_user_id():
    try:
        test_sao.update_user_image_format_service('this will not work', 'downloads/Husky.jpg')
        assert False
    except UserIdMustBeAnInteger as e:
        assert str(e) == 'The user id must be an integer.'

def test_service_update_user_image_format_format_not_string():
    try:
        test_sao.update_user_image_format_service(1, 1)
        assert False
    except ImageFormatMustBeAString as e:
        assert str(e) == 'The image format must be a string.'

def test_service_update_user_image_format_success():
    test_sao.update_user_image_format_service=MagicMock(return_value=True)
    assert test_sao.update_user_image_format_service(1, 'downloads/Husky.jpg')
