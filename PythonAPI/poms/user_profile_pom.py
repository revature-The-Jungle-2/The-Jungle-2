from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.safari.webdriver import WebDriver
class UserProfile:

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

    def profile_picture(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/div/div[6]/div[1]/input")
        return element

    def edit_profile_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/div/div[6]/div[4]/button")
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

    # WebElement
    # upload_file = driver.findElement(By.xpath("//input[@id='file_up']"));
    #
    # upload_file.sendKeys("C:/Users/Sonali/Desktop/upload.png")

