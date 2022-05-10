package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Keys;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.awt.*;
import java.time.Duration;

import static endtoendTests.runner.TestRunner.driver;

public class UnregisteredLoginSadPath {

//    Actions actions = new Actions(driver);
//    @Given("i am on the login page")
//    public void i_am_on_the_login_page() {
//        driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html");
//    }
//    @When("i enter a username")
//    public void i_enter_a_username() {
//        TestRunner.loginPage.sendKeysToUsernameLogin("maty");
//    }
//    @When("i enter a password")
//    public void i_enter_a_password() {
//        TestRunner.loginPage.sendKeysToPasswordLogin("password");
//    }
//    @When("i click the login submit button")
//    public void i_click_the_login_submit_button() throws AWTException {
//        Robot robot = new Robot();
//        robot.mouseMove(50, 50);
//        actions.click().build().perform();
//        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
//        TestRunner.loginPage.clickLoginButton();
//    }
//    Actions act = new Actions(driver);
//    @Then("i should be informed of incorrect credentials and remain on the login page")
//    public void i_should_be_informed_of_incorrect_credentials_and_remain_on_the_login_page() {
//        // Write code here that turns the phrase above into concrete actions
//        WebDriverWait exWait = new WebDriverWait(driver, Duration.ofSeconds(4));
//        exWait.until(ExpectedConditions.urlToBe("\"http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html"));
//        String title = driver.getCurrentUrl();
//        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html", title);
//
//        throw new io.cucumber.java.PendingException();
//    }
}
