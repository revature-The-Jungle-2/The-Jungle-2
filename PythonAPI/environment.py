from behave.runner import Context
from selenium import webdriver
#from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.group_post_pom import GroupPost
from poms.dm_user_profile_pom import UserProfile
from poms.post_feed_pom import PostFeed


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe") #change this as needed
    context.driver.maximize_window()
    #context.driver = WebDriver()
    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###
    context.user_profile_pom = UserProfile(context.driver)
    context.group_post_p = GroupPost(context.driver)
    context.post_feed_p = PostFeed(context.driver)

    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
