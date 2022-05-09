from behave import given, when, then
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the grouppage home page')
def step_impl(context):
    context.driver.get("file:///C:/Users/master/Desktop/The-Jungle-2/FrontEnd/grouppage/group-page.html")


@when(u'I enter the {groupname} in the group name text box')
def step_impl(context, groupname: str):
    context.create_group.group_name().send_keys(groupname)



@when(u'I enter the {description} in the description text box')
def step_impl(context, description: str):
    context.create_group.group_description().send_keys(description)


@when(u'I click the Add Group button')
def step_impl(context):
    context.create_group.add_group_button().click()


@then(u'I get a message created the group successfully')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(alert_is_present())
