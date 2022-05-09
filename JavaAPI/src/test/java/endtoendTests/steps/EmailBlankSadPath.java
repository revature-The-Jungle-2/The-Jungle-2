package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Keys;
import org.openqa.selenium.interactions.Actions;

import static endtoendTests.runner.TestRunner.driver;

public class EmailBlankSadPath {
    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    Actions act = new Actions(driver);
//    @Given("i am on the registration page")
//    public void i_am_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }
    @When("i leave the email blank i am told the email must be present or in correct format")
    public void i_leave_the_email_blank_i_am_told_the_email_must_be_present_or_in_correct_format() {
        TestRunner.signupPage.clickSignupFirstName();
        TestRunner.signupPage.sendKeysToFirstNameSignup("Luna");
        TestRunner.signupPage.clickSignupLastName();
        TestRunner.signupPage.sendKeysToLastNameSignup("Bear");
        TestRunner.signupPage.clickSignupEmail();
        TestRunner.signupPage.sendKeysSignupEmail("");
        act.sendKeys(Keys.TAB).build().perform();
        TestRunner.signupPage.sendKeysSignupBirthdate("19901121");
        TestRunner.signupPage.clickSignupUsername();
        TestRunner.signupPage.sendKeysSignupUsername("LunaBear" + b);
        TestRunner.signupPage.clickSignupPassword();
        TestRunner.signupPage.sendKeysSignupPassword("password");
        // no button to click so commented out
//        TestRunner.signupPage.clickSignupButton()
    }
//    @Then("i remain on the registration page")
//    public void i_remain_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }
}
