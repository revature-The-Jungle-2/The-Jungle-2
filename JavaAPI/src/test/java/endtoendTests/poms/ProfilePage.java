package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ProfilePage {
    private WebDriver driver;


    private By friendSearchBar = By.id("search-inputbar");
    private By friendSearchButton = By.id("searchButton");
    private By createANewPost = By.id("updateProfileEditProfileBtn");
    private By userImageFileInput = By.id("userImageFileInput");
    private By updateProfileEditButton = By.id("updateProfileEditProfileBtn");
    private By chatButton = By.xpath("/html/body/div/div/div[5]/div[1]/a/span");
    private By groupButton = By.xpath("/html/body/div/div/div[5]/div[2]/a/img");
    private By aboutMeTextField = By.id("userAboutMeInput");
    private By userBirthdayInput = By.id("userBirthdateInput");
    private By saveChangesEditProfileButton = By.id("updateProfileModalBtn");
    private By closeEditProfileButton = By.id("updateProfileCloseModalBtn");

}
