from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
# add_cooki

@given(u'I am on the grouppage home page')
def step_impl(context):
    context.driver.get("C:/Users/Yeonghwan Choi/Desktop/The-Jungle-2/FrontEnd/grouppage/group-page.html")
# file:///C:/Users/Yeonghwan%20Choi/Desktop/novo_home.html"

@when(u'I enter the {groupname} in the group name text box')
def step_impl(context, groupname: str):
    context.groupPage.groupName().send_keys(groupname)


@when(u'I enter the not much to know in the {description} text box')
def step_impl(context, description):
    context.groupPage.groupAbout().send_keys(description)


@when(u'I click the Add Group button')
def step_impl(context):
    context.groupPage.add_group_button().click()


@then(u'I get a message created the group successfully')
def step_impl(context):
    WebDriverWait(context.driver, 4)
    assert context.groupPage.get_message().get_attribute('textContent') == "Group created successfully!"
