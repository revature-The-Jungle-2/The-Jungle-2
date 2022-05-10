from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class GroupPost:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def input_password(self):
        element: WebElement = self.driver.find_element(By.XPATH, "//*[@id='passcodeInput']")
        return element

    def welcome_text(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[1]/div[1]")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "//*[@id='submitLogin']")
        return element

    def groups_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/div/comment()[2]")
        return element

