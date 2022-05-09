from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.safari.webdriver import WebDriver
class UserProfile:

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

    def profile_picture(self):
        element: WebElement = self.driver.find_element(By.ID, "userImageFileInput")
        return element

    def edit_profile_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateProfileEditProfileBtn")
        return element

    def about_me_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userAboutMeInput")
        return element

    def birthday_input(self):
        element: WebElement = self.driver.find_element(By.ID, "userBirthdateInput")
        return element

    def save_changes_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateProfileModalBtn")
        return element

    def close_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateProfileCloseModalBtn")
        return element

    def follower_button(self):
        element: WebElement = self.driver.find_element(By.ID, "FIND OUT LATER")
        return element
