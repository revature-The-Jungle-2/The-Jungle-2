from selenium.webdriver.support import expected_conditions as ec
import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the group login page')
def step_impl(context):
    context.driver.get('file:///C:/Users/Will/Desktop/The-Jungle-2/FrontEnd/loginpage/login.html')


@when(u'I enter my group {username}')
def enter_username(context, username: str):
    context.group_post_p.username_input().send_keys(username)


@when(u'I type in my new group {password}')
def enter_password(context, password: str):
    context.group_post_p.input_password.send_keys(password)


@when(u'I click the welcome back')
def click_welcome(context):
    context.group_post_p.welcome_text().click()


@when(u'I click the login button')
def click_log_in(context):
    # WebDriverWait(context.driver, 10).until(
    #     ec.element_to_be_clickable((By.ID, "submitLogin")))
    context.group_post_p.login_button().click()


@then(u'I am on the profile page')
def home_screen(context):
    WebDriverWait(context.driver, 10).until(title_contains("Home"))
    assert context.driver.title == "Home"

# @given(u'I am on the profile page')
# def profile_page(context):
#     context.driver.get('profile.html')
