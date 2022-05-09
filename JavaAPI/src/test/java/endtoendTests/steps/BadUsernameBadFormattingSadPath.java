package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Keys;
import org.openqa.selenium.interactions.Actions;

import static endtoendTests.runner.TestRunner.driver;

public class BadUsernameBadFormattingSadPath {
//    @Given("i am on the registration page")
//    public void i_am_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }

    Actions act = new Actions(driver);
    @When("i fail to enter a properly formatted username i am told the username is missing or must be properly formatted")
    public void i_fail_to_enter_a_properly_formatted_username_i_am_told_the_username_is_missing_or_must_be_properly_formatted() {
        // Write code here that turns the phrase above into concrete actions
//        TestRunner.signupPage.clickSignupFirstName();
//        TestRunner.signupPage.sendKeysToFirstNameSignup("Matt");
//        TestRunner.signupPage.clickSignupLastName();
//        TestRunner.signupPage.sendKeysToLastNameSignup("Ballard");
//        TestRunner.signupPage.clickSignupEmail();
//        TestRunner.signupPage.sendKeysSignupEmail("something@something.com");
//        act.sendKeys(Keys.TAB).build().perform();
//        TestRunner.signupPage.sendKeysSignupBirthdate("19901121");
//        TestRunner.signupPage.clickSignupUsername();
//        TestRunner.signupPage.sendKeysSignupUsername("this is a bad username");
//        TestRunner.signupPage.clickSignupPassword();
//        TestRunner.signupPage.sendKeysSignupPassword("password");
//        throw new io.cucumber.java.PendingException();
    }
//    @Then("i remain on the registration page")
//    public void i_remain_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }

}
