from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver

 
from poms.dm_user_profile_pom import UserProfile


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe") #change this as needed
    context.driver.set_window_size(1920, 1080)
    #context.driver = WebDriver()
    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###
    context.user_profile_pom = UserProfile(context.driver)



    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
