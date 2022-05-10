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

public class RegisteredUserAccessUseChat {

    Actions actions = new Actions(driver);

    @Given("i am logged in an on my profile page")
    public void i_am_logged_in_an_on_my_profile_page() throws AWTException {

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


     @When("i click on the chat link")
   public void i_click_on_the_chat_link() {
        TestRunner.chatPage.clickChatLink();
     }


    @When("i am on the chat page i enter a message in the message input")
    public void i_am_on_the_chat_page_i_enter_a_message_in_the_message_input() {
        TestRunner.chatPage.sendKeysToWriteMessage("test");
    }


    @When("i click on the send message button")
    public void i_click_on_the_send_message_button() {
        TestRunner.chatPage.clickMessageButton();
    }

    @Then("my message is seen in the chat window")
    public void my_message_is_seen_in_the_chat_window() {
        TestRunner.chatPage.sendKeysToMessageButton("test");


    }

}