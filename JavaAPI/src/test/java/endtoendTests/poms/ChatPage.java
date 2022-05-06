package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

public class ChatPage {
    WebDriver driver;

    private By searchBox = By.id("search-container");
    private By writeMessage = By.xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/div/div/input");

    public ChatPage(WebDriver driver) {
        this.driver = driver;

        PageFactory.initElements(driver,this);
    }
}
