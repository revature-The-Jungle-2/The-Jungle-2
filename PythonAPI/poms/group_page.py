from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class GroupPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def groupName(self):
        element: WebElement = self.driver.find_element(By.ID, "groupName")
        return element

    def groupAbout(self):
        element: WebElement = self.driver.find_element(By.ID, "groupAbout")
        return element

    def add_group_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitCreateGroup")
        return element

    def get_message(self):
        element: WebElement = self.driver.find_element(By.ID, "messageGroupCreated")
        return element

    def select_group(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="groups-div"]/div[1]/div')
        return element

    def get_title(self):
        return self.driver.title

    def join_group(self):
        element: WebElement = self.driver.find_element(By.ID, "submitJoinGroup")
        return element

    def get_message_join(self):
        element: WebElement = self.driver.find_element(By.ID, "groupNotJoined")
        return element

