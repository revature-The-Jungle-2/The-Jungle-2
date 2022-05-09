from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
<<<<<<< HEAD
<<<<<<< HEAD
    context.driver.get("C:/Users/Almas/Desktop/The-Jungle-2/PythonAPI/chromedriver.exe")


@when(u'I enter my <username>')
def step_impl(context):
    context.dm_user_profile_pom.user_username().

=======
    context.driver.get('')
=======
    context.driver.get('login.html')
>>>>>>> e8dd1ab089cb9077a859322f7df5f8f2124b21a0

@when(u'I enter my {username}')
def step_impl(context, username):
    context.user_profile_pom.username_input().send_keys(username)
>>>>>>> cc5254cb60cc1a0b4d95e6fc925da4f05974e8e0

@when(u'I enter my {password}')
def step_impl(context, password):
    context.user_profile_pom.password_input().send_keys(password)

@when(u'I click the login button')
def step_impl(context):
    context.user_profile_pom.login_button().click()

@when(u'I click the profile picture')
def step_impl(context):
    context.user_profile_pom.profile_picture().click()

@when(u'I choose my {picture}')
def step_impl(context, picture):
    context.user_profile_pom.choose_picture().send_keys(picture)

@then(u'I am back on the profile page')
def step_impl(context):
    assert context.driver.title == "Home"

@when(u'I click the edit profile button')
def step_impl(context):
    context.user_profile_pom.edit_profile_button().click()

@when(u'I enter my {about_me} incorrectly')
def step_impl(context, about_me):
    context.user_profile_pom.about_me_input().send_keys(about_me)

@when(u'I enter my {birthday} incorrectly')
def step_impl(context, birthday):
    context.user_profile_pom.birthday_input().send_keys(birthday)

@when(u'I enter my {about_me}')
def step_impl(context, about_me):
    context.user_profile_pom.about_me_input().send_keys(about_me)

@when(u'I enter my {birthday}')
def step_impl(context, birthday):
    context.user_profile_pom.birthday_input().send_keys(birthday)

@when(u'I click the save changes button')
def step_impl(context):
    context.user_profile_pom.save_changes_button().click()

@then(u'I click the close button')
def step_impl(context):
    context.user_profile_pom.close_button().click()

@when(u'I click on my follower')
def step_impl(context):
    context.user_profile_pom.follower_button().click()

@then(u'I am on their profile')
def step_impl(context):
    assert context.driver.title == "profile-page.html"