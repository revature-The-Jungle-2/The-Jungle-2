from behave.runner import Context
from selenium import webdriver


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")  # change this as needed
    # context.
    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
