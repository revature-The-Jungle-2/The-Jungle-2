package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.awt.*;
import java.time.Duration;

import static endtoendTests.runner.TestRunner.driver;
import static endtoendTests.runner.TestRunner.signupPage;

public class UnregisteredUserSignUp {
    int min = 1;
    int max = 10000;
    int b = (int) (Math.random() * (max - min + 1) + min);
    int c = (int) (Math.random() * (max - min + 1) + min);
    Actions act = new Actions(driver);

    Actions actions = new Actions(driver);

    //    @Given("i am on the registration page")
//    public void i_am_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }
    @When("i enter my profile info correctly")
    public void i_enter_my_profile_info_correctly() throws AWTException {
        TestRunner.signupPage.clickSignupFirstName();
        TestRunner.signupPage.sendKeysToFirstNameSignup("Jane");
        TestRunner.signupPage.clickSignupLastName();
        TestRunner.signupPage.sendKeysToLastNameSignup("Doe");
        TestRunner.signupPage.clickSignupEmail();
        TestRunner.signupPage.sendKeysSignupEmail("JaneDoe"+b+"@gmail.com");
        act.sendKeys(Keys.TAB).build().perform();
        TestRunner.signupPage.sendKeysSignupBirthdate("19901121");
        TestRunner.signupPage.clickSignupUsername();
        TestRunner.signupPage.sendKeysSignupUsername("JaneDoe"+c);
        TestRunner.signupPage.clickSignupPassword();
        TestRunner.signupPage.sendKeysSignupPassword("janedoe1");
        Robot robot = new Robot();
        robot.mouseMove(50, 50);
        actions.click().build().perform();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        TestRunner.signupPage.clickSignupButton();
    }

    @When("i click the registration submit button")
    public void i_click_the_registration_submit_button() {
        TestRunner.signupPage.clickSignupButton();
    }

    @Then("i am redirected to the profile page")
    public void i_am_redirected_to_the_profile_page() {
        WebDriverWait exWait = new WebDriverWait(driver, Duration.ofSeconds(4));
        exWait.until(ExpectedConditions.urlToBe("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html"));
        String title = driver.getCurrentUrl();
        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/profilepage/profile-page.html", title);
    }
}

