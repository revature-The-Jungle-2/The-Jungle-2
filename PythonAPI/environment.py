from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver
from poms.create_group_home import createGroupHome
from poms.join_group_home import joinGroupHome

def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")  # change this as needed
    context.groupPage = GroupPage(context.driver)
    context.individualGroupPage = individualGroupPage(context.driver)
    context.UserProfile = UserProfile(context.driver)
    


    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###
    context.create_group = createGroupHome(context.driver)
    context.join_group = joinGroupHome(context.driver)
    context.driver.implicitly_wait(1)

    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

def after_all(context: Context):
    context.driver.quit()
