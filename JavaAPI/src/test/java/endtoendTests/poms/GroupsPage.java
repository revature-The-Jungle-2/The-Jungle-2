package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class GroupsPage {
    WebDriver driver;

    private By groupName = By.id("groupName");
    private By groupDescription = By.id("groupAbout");
    private By addGroupButton = By.id("submitCreateGroup");
    private By groupsButton = By.xpath("/html/body/div/div/div[1]/div[3]/div[2]/a/img");

}
