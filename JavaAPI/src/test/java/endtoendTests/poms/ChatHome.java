package endtoendTests.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class ChatHome {
    private WebDriver driver;

    // you can manually set the web elements you want to interact with by using the By class
    private By searchBar = By.id("searchInput");
    private By searchButton = By.className("pure-button");

    public ChatHome(WebDriver driver){
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements
        PageFactory.initElements(driver,this);
    }

    @FindBy(id = "js-link-box-en")
    public WebElement english;


    // you can also avoid using the page factory and manually search for the elements yourself
    public void sendKeysToSearchbar(String input){
        driver.findElement(searchBar).sendKeys(input);
    }

    public void clickSearchButton(){
        driver.findElement(searchButton).click();
    }

}
