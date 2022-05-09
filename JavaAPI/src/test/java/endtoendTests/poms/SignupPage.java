package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.devtools.v96.indexeddb.model.Key;
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

    public void clickSignupFirstName(){
        driver.findElement(signupFirstName).click();
    }

    public void sendKeysToFirstNameSignup(String input){
        driver.findElement(signupFirstName).sendKeys(input);
    }

    public void clickSignupLastName(){
        driver.findElement(signupLastName).click();
    }

    public void sendKeysToLastNameSignup(String input){
        driver.findElement(signupLastName).sendKeys(input);
    }

    public void clickSignupEmail(){
        driver.findElement(signupEmail).click();
    }

    public void sendKeysSignupEmail(String input){
        driver.findElement(signupEmail).sendKeys(input);
    }

    // Using tab instead for birthday selection bug
//    public void clickSignupBirthdate(){
//        driver.findElement(signupBirthDate).click();
//    }

    public void sendKeysSignupBirthdate(String input){
        driver.findElement(signupBirthDate).sendKeys(input);
    }

    public void clickSignupUsername(){
        driver.findElement(signupUsername).click();
    }

    public void sendKeysSignupUsername(String input){
        driver.findElement(signupUsername).sendKeys(input);
    }

    public void clickSignupPassword(){
        driver.findElement(signupPassword).click();
    }

    public void sendKeysSignupPassword(String input){
        driver.findElement(signupPassword).sendKeys(input);
    }

    public void clickSignupButton(){driver.findElement(signupButton).click();

    }



}
