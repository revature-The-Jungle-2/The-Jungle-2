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
    private By chatButton = By.className("linkChat");
    private By groupButton = By.className("linkGroups");
}
