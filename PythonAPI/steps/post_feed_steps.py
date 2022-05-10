from behave import given, when, then
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the Login Page')
def step_impl(context):
    context.driver.get("https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css")


@when(u'I type in my {Username}')
def step_impl(context, username: str):
    context.post_feed_home.get.username.send_keys(username)


@when(u'I enter my {Password}')
def step_impl(context, password:str):
    context.post_feed_home.get.password.send_keys(password)


@when(u'I click Login button')
def step_impl(context):
    context.post_feed_home.login_button().click()


@then(u'I am on the profile page and can see the post feed')
def home_screen(context):
    WebDriverWait(context.driver, 10).until(title_contains("Home"))
    assert context.driver.title == "Home"


#

# @when(u'I accept the alert button')
# def step_impl(context):
#     context.post_feed_home.alert_button().click()
#
# @then(u'I can view the Post Feed')
# def step_impl(context):
#     context.driver.get()



# <<<<<<< HEAD
# =======
# @when(u'I enter my Username')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I enter my Username')
#
#
# @when(u'I enter my Password')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I enter my Password')
#
#
# @when(u'I click Login')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click Login')
#
#
# @then(u'I can see posts in my feed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I can see posts in my feed')
#
#
# @given(u'I am on the Visit Profile Page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I am on the Profile Page')
#
#
# @when(u'I click on the "Search for Friends" button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on the "Search for Friends" button')
#
#
# @then(u'I can view the Post Feed for my friends')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I can view the Post Feed for my friends')
#
#
# @given(u'I am on the Profile Page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I am on the Profile Page')
#
#
# @when(u'I input post id')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I input post id')
#
#
# @when(u'I click Delete Post')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click Delete Post')
#
#
# @then(u'My post id deleted')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then My post id deleted')
# >>>>>>> e8d884ad0306f4faaf7406617cc49e97cff0e922
