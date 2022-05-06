package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class GroupsPage {
    WebDriver driver;

    private By groupName = By.id("groupName");
    private By groupDescription = By.id("groupAbout");
    private By addGroupButton = By.id("submitCreateGroup");
    private By groupsButton = By.className("x-icon");

}
