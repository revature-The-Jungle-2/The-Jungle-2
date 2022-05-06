from behave.runner import Context
from selenium import webdriver

from poms.create_group_home import createGroupHome
from poms.join_group_home import joinGroupHome


def before_all(context: Context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\master\Desktop\The-Jungle-2\PythonAPI\features\chromedriver.exe") #change this as needed

    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###
    context.create_group = createGroupHome(context.driver)
    context.join_group = joinGroupHome(context.driver)
    context.driver.implicitly_wait(1)



    ###PUT YOUR POM CONTEXTS BETWEEN THESE LINES.###

    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()