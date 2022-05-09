from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class individualGroupPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def groups(self):
        element: WebElement = self.driver.find_element(By.ID, "groupLink-1")
        return element

    def get_title(self):
        return self.driver.title

    def join_group(self):
        element: WebElement = self.driver.find_element(By.ID, "submitJoinGroup")
        return element

    def get_alert(self):
        return self.driver.switch_to.alert