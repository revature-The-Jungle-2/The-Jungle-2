package endtoendTests.steps;

import endtoendTests.poms.SignupPage;
import endtoendTests.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.testng.Assert;


public class EmailBadFormattingSadPath {
    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    int c = (int)(Math.random()*(max-min+1)+min);

    @Given("i am on the registration page")
    public void i_am_on_the_registration_page() {
//        "file://C:\\"+System.getenv("HOMEPATH")+"\\Desktop\\The-Jungle-2\\FrontEnd\\login.html"
        TestRunner.driver.get("C:\\java\\jungle3\\The-Jungle-2\\FrontEnd\\registrationpage\\sign-up.html");
//        throw new io.cucumber.java.PendingException();
    }
    @When("i fail to enter a properly formatted email i am told the email must be present or in correct format")
    public void i_fail_to_enter_a_properly_formatted_email_i_am_told_the_email_must_be_present_or_in_correct_format() {
        TestRunner.signupPage.clickSignupFirstName();
        TestRunner.signupPage.sendKeysToFirstNameSignup("Luna");
        TestRunner.signupPage.clickSignupLastName();
        TestRunner.signupPage.sendKeysToLastNameSignup("Bear");
        TestRunner.signupPage.clickSignupEmail();
        TestRunner.signupPage.sendKeysSignupEmail("LunaBearasdfasdfasdfdasfasdfasdfasdfasdfsadfsadfasdfasdfsadfasdfasdfasdfsadfasdfsadfasdfsadfasdfasdfasdf"+ b + "@gmail.com");
        TestRunner.signupPage.clickSignupBirthdate();
        TestRunner.signupPage.sendKeysSignupBirthdate("11121990");
        TestRunner.signupPage.clickSignupUsername();
        TestRunner.signupPage.sendKeysSignupUsername("LunaBear" + c);
        TestRunner.signupPage.clickSignupPassword();
        TestRunner.signupPage.sendKeysSignupPassword("password");
        TestRunner.signupPage.clickSignupButton();
    }
    @Then("i remain on the registration page")
    public void i_remain_on_the_registration_page() {
        TestRunner.wait.until(ExpectedConditions.titleIs("Home"));
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals("Home", title);
    }
}
