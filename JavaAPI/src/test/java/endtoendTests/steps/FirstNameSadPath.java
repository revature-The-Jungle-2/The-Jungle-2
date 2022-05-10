package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Keys;
import org.openqa.selenium.interactions.Actions;

import static endtoendTests.runner.TestRunner.driver;

public class FirstNameSadPath {
    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    int c = (int)(Math.random()*(max-min+1)+min);
    Actions act = new Actions(driver);
    String url = driver.getCurrentUrl();


//    @Given("i am on the registration page")
//    public void i_am_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }
    @When("i fail to enter a firstname i am told the firstname must be present")
    public void i_fail_to_enter_a_firstname_i_am_told_the_firstname_must_be_present() {
        TestRunner.signupPage.clickSignupFirstName();
        TestRunner.signupPage.sendKeysToFirstNameSignup("");
        TestRunner.signupPage.clickSignupLastName();
        TestRunner.signupPage.sendKeysToLastNameSignup("Bear");
        TestRunner.signupPage.clickSignupEmail();
        TestRunner.signupPage.sendKeysSignupEmail("LunaBear"+ b + "@gmail.com");
        act.sendKeys(Keys.TAB).build().perform();
        TestRunner.signupPage.sendKeysSignupBirthdate("19901121");
        TestRunner.signupPage.clickSignupUsername();
        TestRunner.signupPage.sendKeysSignupUsername("LunaBear" + c);
        TestRunner.signupPage.clickSignupPassword();
        TestRunner.signupPage.sendKeysSignupPassword("password" + b + b + b + b + b + b + b + b + b + b);
    }
//    @Then("i remain on the registration page")
//    public void i_remain_on_the_registration_page() {
//        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();
//    }
}
