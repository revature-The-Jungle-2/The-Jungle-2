from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am logged in')
def step_impl(context):
    context.driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html")
    context.post_feed_p.username_input().send_keys("fool")
    context.post_feed_p.password_input().send_keys("fool")
    context.post_feed_p.password_input().send_keys(Keys.TAB)
    context.post_feed_p.login_button().click()


@then(u'I am on the profile page and can see the post feed')
def home_screen(context):
    WebDriverWait(context.driver, 10).until(title_contains("Home"))
    assert context.driver.title == "Home"


# @when(u'I accept the alert button')
# def step_impl(context):
#     context.post_feed_home.alert_button().click()
