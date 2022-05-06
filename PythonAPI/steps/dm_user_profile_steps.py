from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('')

@when(u'I enter my <username>')
def step_impl(context, username):
    context.user_profile_pom.username_input().send_keys(username)

@when(u'I enter my <password>')
def step_impl(context, password):
    context.user_profile_pom.password_input().send_keys(password)

@when(u'I click the login button')
def step_impl(context):
    context.user_profile_pom.login_button().click()

@when(u'I click the profile picture')
def step_impl(context):
    context.user_profile_pom.profile_picture().click()

@when(u'I choose my downloads/Husky.jpg')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I choose my downloads/Husky.jpg')

@then(u'I am back on the profile page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am back on the profile page')

@when(u'I click the edit profile button')
def step_impl(context):
    context.user_profile_pom.edit_profile_button().click()

@when(u'I enter my <about_me> incorrectly')
def step_impl(context, about_me):
    context.user_profile_pom.about_me_input().send_keys(about_me)

@when(u'I enter my <birthday> incorrectly')
def step_impl(context, birthday):
    context.user_profile_pom.birthday_input().send_keys(birthday)

@when(u'I enter my <about_me>')
def step_impl(context, about_me):
    context.user_profile_pom.about_me_input().send_keys(about_me)

@when(u'I enter my <birthday>')
def step_impl(context, birthday):
    context.user_profile_pom.birthday_input().send_keys(birthday)

@when(u'I click the save changes button')
def step_impl(context):
    context.user_profile_pom.save_changes_button().click()

@then(u'I am left in the pop up')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am left in the pop up')

@when(u'I click on my follower')
def step_impl(context):
    context.user_profile_pom.follower_button().click()

@then(u'I am on their profile')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am on their profile')
