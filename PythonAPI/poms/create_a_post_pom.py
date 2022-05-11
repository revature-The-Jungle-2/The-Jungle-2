from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver


class CreatePostHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passcodeInput")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitLogin")
        return element

    def post_text(self):
        element: WebElement = self.driver.find_element(By.ID, "postText")
        return element

    def image_input(self):
        element: WebElement = self.driver.find_element(By.ID, "imageFile")
        return element

    def post_submit(self):
        element: WebElement = self.driver.find_element(By.XPATH, "//*[@id='createPostForm']/button")
        return element

    def open_post_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "updateProfileEditProfileBtn")
        return element
