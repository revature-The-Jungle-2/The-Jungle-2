package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class SignupPage {
    WebDriver driver;

    //Signup Page
    private By signupFirstName = By.id("signup-firstname");
    private By signupLastName = By.id("signup-lastname");
    private By signupEmail = By.id("signup-email");
    private By signupBirthDate = By.id("signup-bdate");
    private By signupUsername = By.id("signup-username");
    private By signupPassword = By.id("signup-password");
    private By signupButton = By.id("signup-submit"); //may need to be clicked twice

    public SignupPage(WebDriver driver){
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements
        PageFactory.initElements(driver,this);
    }

}
