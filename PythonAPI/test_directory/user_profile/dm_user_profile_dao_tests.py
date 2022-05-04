from data_access_layer.implementation_classes.user_profile_dao import UserProfileDAOImp
from entities.user import User

test_dao = UserProfileDAOImp()

def test_get_user_profile_success():
    test_get_user_profile = test_dao.get_user_profile(1)
    assert test_get_user_profile.user_id == 1

def test_update_user_profile_success():
    test_user = User(1, 'Dylan', 'Mercer', 'dylanmercer@email.com', 'username', 'password', 'about', '1/1/1997', 'img')
    test_updated_user_profile = test_dao.update_user_profile(test_user)
    assert test_updated_user_profile.first_name == 'Dylan'

def test_get_user_image_success():
    test_get_user_image = test_dao.get_user_image(1)
    assert test_get_user_image

def test_update_user_image_success():
    test_update_user_image = test_dao.update_user_image(1, 'downloads/Husky-2.jpg')
    assert test_update_user_image

def test_update_user_image_format_success():
    test_updated_image = test_dao.update_user_image_format(1, 'downloads/Husky-2.jpg')
    assert test_updated_image
