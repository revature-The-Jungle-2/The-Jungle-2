from selenium.webdriver.support import expected_conditions as ec
import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('file:///C:/Users/pompa/Desktop/The-Jungle-2/FrontEnd/loginpage/login.html')


@when(u'I enter my {username}')
def enter_username(context, username: str):
    context.user_profile_pom.username_input().send_keys(username)

@when(u'I type in my new {password}')
def enter_password(context, password: str):
    context.user_profile_pom.input_password().send_keys(password)

@when(u'I click the welcome back')
def click_welcome(context):
    context.user_profile_pom.welcome_text().click()




@when(u'I click the login button')
def click_log_in(context):
    # WebDriverWait(context.driver, 10).until(
    #     ec.element_to_be_clickable((By.ID, "submitLogin")))
    context.user_profile_pom.login_button().click()

@when(u'I click the profile {picture}')
def click_prof_pic(context, picture):
    context.user_profile_pom.profile_picture().click()
    context.user_profile_pom.profile_picture().send_keys(picture)

@then(u'I am on the profile page')
def home_screen(context):
    WebDriverWait(context.driver, 10).until(title_contains("Home"))
    assert context.driver.title == "Home"

@given(u'I am on the profile page')
def profile_page(context):
    context.driver.get('profile.html')

@when(u'I click the edit profile button')
def edit_button(context):
    context.user_profile_pom.edit_profile_button().click()

# @when(u'I enter my {about_me} incorrectly')
# def about_me(context, about_me):
#     context.user_profile_pom.about_me_input().send_keys(about_me)

# @when(u'I enter my {birthday} incorrectly')
# def birthday(context, birthday):
#     context.user_profile_pom.birthday_input().send_keys(birthday)

# @when(u'I enter my {about_me}')
# def about_me_2(context, about_me):
#     context.user_profile_pom.about_me_input().send_keys(about_me)

# @when(u'I enter my {birthday}')
# def birthday_2(context, birthday):
#     context.user_profile_pom.birthday_input().send_keys(birthday)

@when(u'I click the save changes button')
def save_changes(context):
    context.user_profile_pom.save_changes_button().click()

@then(u'I click the close button')
def close(context):
    context.user_profile_pom.close_button().click()

@when(u'I click on my follower')
def click_follower(context):
    context.user_profile_pom.follower_button().click()

@then(u'I am on their profile')
def other_profile(context):
    assert context.driver.title == "profile-page.html"