from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given(u'I am logged in')
def step_impl(context):
    context.driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html")
    context.post_home.username_input().send_keys("fool")
    context.post_home.password_input().send_keys("fool")
    context.post_home.password_input().send_keys(Keys.TAB)
    context.post_home.login_button().click()




@when(u'I click to open the post modal')
def step_impl(context):
    context.post_home.open_post_modal().click()


@when(u'I enter the post text info')
def step_impl(context):
    # need to insert test post info here
    context.post_home.post_text().send_keys("")


@when(u'I enter the image info')
def step_impl(context):
    context.post_home.image_input().send_keys("")



@when(u'I press the submit button')
def step_impl(context):
    context.post_home.post_submit().click()


@then(u'Post is created')
def step_impl(context):
    # need to assert whatever happens afterwards. I havent tried
    raise NotImplementedError(u'STEP: Then Post is created')
