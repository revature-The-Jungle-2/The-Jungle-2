package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.awt.*;
import java.time.Duration;

import static endtoendTests.runner.TestRunner.driver;
import static endtoendTests.runner.TestRunner.teardown;

public class RegisteredUserLoginProfilePage {
    Actions actions = new Actions(driver);






    @Given("i am on the log in page")
    public void i_am_on_the_log_in_page() {
        driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html");
    }
    @When("i enter a username")
    public void i_enter_a_username() {
        TestRunner.loginPage.sendKeysToUsernameLogin("matty");
    }
    @When("i enter a password")
    public void i_enter_a_password() {
        TestRunner.loginPage.sendKeysToPasswordLogin("password");
    }
    @When("i click the login submit button")
    public void i_click_the_login_submit_button() throws AWTException {
        Robot robot = new Robot();
        robot.mouseMove(50,50);
        actions.click().build().perform();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        TestRunner.loginPage.clickLoginButton();

    }
    @Then("i am logged in and redirected to my profile page")
    public void i_am_logged_in_and_redirected_to_my_profile_page() {
        WebDriverWait exWait = new WebDriverWait(driver, Duration.ofSeconds(4));
        exWait.until(ExpectedConditions.urlToBe("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html"));
        String title = driver.getCurrentUrl();
        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html", title);
    }

}
