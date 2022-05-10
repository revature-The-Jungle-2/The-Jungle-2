package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class GroupsPage {
    WebDriver driver;

    private By groupName = By.id("groupName");
    private By groupDescription = By.id("groupAbout");
    private By addGroupButton = By.id("submitCreateGroup");
    private By groupButton = By.xpath("/html/body/div/div/div[1]/div[3]/div[2]/a/img");

    public GroupsPage(WebDriver driver){
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements
        PageFactory.initElements(driver,this);
    }

    public void clickGroupButton() { driver.findElement(groupButton).click(); }

    public void writeGroupName(String input) { driver.findElement(groupName).sendKeys(input); }

    public void writeGroupDescription(String input) { driver.findElement(groupDescription).sendKeys(input); }

    public void clickAddGroupButton() {driver.findElement(addGroupButton).click(); }

}
