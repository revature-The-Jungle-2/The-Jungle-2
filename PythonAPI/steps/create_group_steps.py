from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
import random


@given(u'I am on the grouppage home page')
def step_impl(context):
    context.driver.get("C:/Users/Yeonghwan Choi/Desktop/The-Jungle-2/FrontEnd/grouppage/group-page.html")


@when(u'I enter the groupname in the group name text box')
def step_impl(context):
    groupname = "group"+str(random.randint(0,9999))
    context.groupPage.groupName().send_keys(groupname)


@when(u'I enter the {description} in the description text box')
def step_impl(context, description):
    context.groupPage.groupAbout().send_keys(description)


@when(u'I click the Add Group button')
def step_impl(context):
    context.groupPage.add_group_button().click()


@then(u'I get a message created the group successfully')
def step_impl(context):
    WebDriverWait(context.driver, 4)
    assert context.groupPage.get_message().get_attribute('textContent') == "Group created successfully!"


@when(u'click on the Groups on the side bar')
def step_impl(context):
    WebDriverWait(context.driver, 4)
    context.groupPage.select_group().click()

@when(u'I am on the individual group page')
def step_impl(context):
    assert context.groupPage.get_title() == "Individual Group Page"


@when(u'I click on the join group button')
def step_impl(context):
    context.groupPage.join_group().click()


@then(u'I get a message joined the group successfully')
def step_impl(context):
    context.groupPage.get_message_join().get_attribute('textContent') == "Group joined."

