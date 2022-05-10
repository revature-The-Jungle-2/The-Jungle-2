package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.awt.*;
import java.time.Duration;

import static endtoendTests.runner.TestRunner.driver;

public class RegisteredUserAccessToGroupChat {

    Actions actions = new Actions(driver);

    @Given("i am logged in and on my profile page")
    public void iAmLoggedInAndOnMyProfilePage() throws AWTException {
        driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html");
        TestRunner.loginPage.sendKeysToUsernameLogin("matty");
        TestRunner.loginPage.sendKeysToPasswordLogin("password");
        Robot robot = new Robot();
        robot.mouseMove(50,50);
        actions.click().build().perform();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        TestRunner.loginPage.clickLoginButton();
        WebDriverWait exWait = new WebDriverWait(driver, Duration.ofSeconds(4));
        exWait.until(ExpectedConditions.urlToBe("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html"));
        String title = driver.getCurrentUrl();
        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html", title);
    }

    @When("i click on the chat button")
    public void iClickOnTheChatButton() {
        TestRunner.chatPage.clickChatLink();
    }

    @When("i am on the chat page i click on a group chat link")
    public void i_am_on_the_chat_page_i_click_on_a_group_chat_link() {
        TestRunner.groupsPage.clickGroupButton();
    }

    @When("i am on the group page and enter a group name")
    public void iAmOnTheGroupPageAndEnterAGroupName() {
        TestRunner.groupsPage.writeGroupName("hello");
    }

    @When("i am on the group page and enter a group description")
    public void iAmOnTheGroupPageAndEnterAGroupDescription() {
        TestRunner.groupsPage.writeGroupDescription("hello");
    }

    @When("i am on the group page i click on the add group button")
    public void iAmOnTheGroupPageIClickOnTheAddGroupButton() {
        TestRunner.groupsPage.clickAddGroupButton();
    }

    @Then("i have access to a that group")
    public void iHaveAccessToAThatGroup() {
        WebDriverWait exWait = new WebDriverWait(driver, Duration.ofSeconds(2));
        exWait.until(ExpectedConditions.urlToBe("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/grouppage/group-page.html"));
        String title = driver.getCurrentUrl();
        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/grouppage/group-page.html", title);
    }
}
