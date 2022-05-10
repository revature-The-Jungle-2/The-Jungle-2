from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class PostFeed:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_username_box(self):
        return self.driver.find_element(By.ID, 'usernameInput')

    def select_password_box(self):
        return self.driver.find_element(By.ID, 'passcodeInput')

    def select_login_button(self):
        return self.driver.find_element(By.ID, 'submitLogin')
