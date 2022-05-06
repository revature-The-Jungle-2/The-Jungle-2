from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class createGroupHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def group_name(self):
        element: WebElement = self.driver.find_element(By.ID, "groupName")
        return element

    def group_description(self):
        element: WebElement = self.driver.find_element(By.ID, "groupAbout")
        return element

    def add_group_button(self):
        element: WebElement =  self.driver.find_element(By.ID, "submitCreateGroup")
        return element

    def get_alert(self):
        return self.driver.switch_to.alert
