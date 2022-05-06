package endtoendTests.steps;

import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class EmailBadFormattingSadPath {
    @Given("i am on the registration page")
    public void i_am_on_the_registration_page() {
//        "file://C:\\"+System.getenv("HOMEPATH")+"\\Desktop\\The-Jungle-2\\FrontEnd\\login.html"
        TestRunner.driver.get("C:\\java\\jungle3\\The-Jungle-2\\FrontEnd\\registrationpage\\sign-up.html");
//        throw new io.cucumber.java.PendingException();
    }
    @When("i fail to enter a properly formatted email i am told the email must be present or in correct format")
    public void i_fail_to_enter_a_properly_formatted_email_i_am_told_the_email_must_be_present_or_in_correct_format() {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }
    @Then("i remain on the registration page")
    public void i_remain_on_the_registration_page() {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }
}
