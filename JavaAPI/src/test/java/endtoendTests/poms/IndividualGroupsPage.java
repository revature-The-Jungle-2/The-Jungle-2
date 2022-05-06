package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class IndividualGroupsPage {
    WebDriver driver;

    private By submitJoinGroup = By.id("submitJoinGroup");
    private By whatsOnYourMind = By.id("postInput");
    private By getWhatsOnYourMindButton = By.id("sendGroupPostButton");
    private By leaveGroupButton = By.id("tbd");


    public IndividualGroupsPage(WebDriver driver){
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements
        PageFactory.initElements(driver,this);
    }
    //Individual Groups Page


}
