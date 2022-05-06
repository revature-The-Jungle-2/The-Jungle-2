package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage {
    private WebDriver driver;

    //Login Page
    private By usernameLogin = By.id("usernameInput");
    private By passwordLogin = By.id("passcodeInput");
    private By loginButton = By.id("submitLogin"); // needs to be clicked twice

    public void clickUsernameLoginField(){
        driver.findElement(usernameLogin).click();
    }

    public void sendKeysToUsernameLogin(String input){
        driver.findElement(usernameLogin).sendKeys(input);
    }

    public void clickPasswordLoginField(){
        driver.findElement(passwordLogin).click();
    }

    public void sendKeysToPasswordLogin(String input){
        driver.findElement(passwordLogin).sendKeys(input);
    }

    public void clickLoginButton(){
        driver.findElement(loginButton).click();
    }



}
