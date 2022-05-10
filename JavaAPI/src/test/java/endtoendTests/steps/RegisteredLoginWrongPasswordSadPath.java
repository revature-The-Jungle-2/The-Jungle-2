package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Keys;
import org.testng.Assert;

import java.time.Duration;

import static endtoendTests.runner.TestRunner.driver;

public class RegisteredLoginWrongPasswordSadPath {
    @Given("i am on the login page")
    public void i_am_on_the_login_page() {
        driver.get("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html");
    }
    @When("i fail to enter a correct password i am told the password must be correct")
    public void i_fail_to_enter_a_correct_password_i_am_told_the_password_must_be_correct() {
        TestRunner.loginPage.clickUsernameLoginField();
        TestRunner.loginPage.sendKeysToUsernameLogin("LunaBear8215");
        TestRunner.loginPage.clickPasswordLoginField();
        TestRunner.loginPage.sendKeysToPasswordLogin("wrongPassword");
    }
//    @When("i click the login submit button")
//    public void i_click_the_login_submit_button() {
//        TestRunner.loginPage.clickLoginButton();
//    }
//    @Then("i should be informed of incorrect credentials and remain on the login page")
//    public void i_should_be_informed_of_incorrect_credentials_and_remain_on_the_login_page() {
//        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
//        String title = driver.getCurrentUrl();
//        Assert.assertEquals("http://the-jungle-2-rev-bucket.s3-website-us-east-1.amazonaws.com/FrontEnd/loginpage/login.html", title);
//    }
}
