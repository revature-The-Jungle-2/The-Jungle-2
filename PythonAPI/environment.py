from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver

 
from poms.dm_user_profile_pom import UserProfile
from poms.group_page import GroupPage
from poms.individual_group_page import individualGroupPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("PythonAPI/features/chromedriver.exe")
    context.groupPage = GroupPage(context.driver)
    context.individualGroupPage = individualGroupPage(context.driver)
    context.UserProfile = UserProfile(context.driver)


    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
