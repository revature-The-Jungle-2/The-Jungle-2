from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


<<<<<<<< HEAD:PythonAPI/poms/post_feed_home.py
class PostFeed:
========
class GroupPost:
>>>>>>>> e8d884ad0306f4faaf7406617cc49e97cff0e922:PythonAPI/poms/group_post_pom.py
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_box(self):
        return self.driver.find_element(By.ID, 'usernameInput')

    def select_password_box(self):
        return self.driver.find_element(By.ID, 'passcodeInput')

    def select_login_button(self):
        return self.driver.find_element(By.ID, 'submitLogin')

    def select_post_column(self):
        return self.driver.find_element(By.ID, 'post column')

