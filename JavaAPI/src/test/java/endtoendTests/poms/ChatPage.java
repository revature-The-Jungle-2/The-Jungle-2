package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class ChatPage {
    WebDriver driver;


    private By searchBox = By.id("search-container");
    private By writeMessage = By.xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/div/div/input");
    private By chatLink = By.xpath("/html/body/div/div/div[1]/div[2]/div[1]/a/span");
    private By groupLink = By.xpath("/html/body/div/div/div[1]/div[2]/div[2]/a/span");
    private By messageButton = By.xpath("")

    public ChatPage(WebDriver driver) {
        this.driver = driver;

        PageFactory.initElements(driver,this);
    }

    public void clickChatLink() { driver.findElement(chatLink).click(); }

    public void sendKeysToChatLink(String input) { driver.findElement(chatLink).sendKeys(input); }

    public void clickWriteMessage(String input) { driver.findElement(writeMessage).click(); }

    public void sendKeysToWriteMessage(String input) { driver.findElement(writeMessage).click(); }

    public void sendKeysToWriteMessage(String input){ driver.findElement(writeMessage).sendKeys(input); }

    public void clickMessageButton() { driver.findElement(messagedButton).click(); }

    public void sendKeysToMessageButton(String input) { driver.findElement(messageButton).sendKeys(input); }



}
