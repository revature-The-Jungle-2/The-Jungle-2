from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class PostFeed:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def password_input(self):
        element: WebElement = self.driver.find_element(By.XPATH, "//*[@id='passcodeInput']")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "//*[@id='submitLogin']")
        return element
