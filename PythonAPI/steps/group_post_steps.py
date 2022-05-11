from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import title_contains, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


# @given(u'I am logged in')
# def step_impl(context):
#     context.driver.get(
#         "http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html")
#     context.post_feed_p.username_input().send_keys("fool")
#     context.post_feed_p.password_input().send_keys("fool")
#     context.post_feed_p.password_input().send_keys(Keys.TAB)
#     context.post_feed_p.login_button().click()


@when(u'I am on the profile page and can see the post feed')
def home_screen_group(context):
    WebDriverWait(context.driver, 10).until(title_contains("Home"))
    assert context.driver.title == "Home"


@when(u'I select groups')
def groups_click(context):
    WebDriverWait(context.driver, 2).until(element_to_be_clickable(context.group_post_p.groups_button()))
    context.group_post_p.groups_button().click()

# @when(u'I accept the alert button')
# def step_impl(context):
#     context.group_post_p.alert_button().click()

@when(u'I select groups the second time')
def groups_click_two(context):
    WebDriverWait(context.driver, 2).until(element_to_be_clickable(context.group_post_p.groups_button_two()))
    context.group_post_p.groups_button_two().click()


@then(u'I am on the page to make a group post')
def group_post_page(context):
    WebDriverWait(context.driver, 2).until(title_contains("Individual Group Page"))
    assert context.driver.title == "Individual Group Page"
