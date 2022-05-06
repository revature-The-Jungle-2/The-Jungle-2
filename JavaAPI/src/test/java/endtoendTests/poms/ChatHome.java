//package endtoendTests.poms;
//
//import org.openqa.selenium.By;
//import org.openqa.selenium.WebDriver;
//import org.openqa.selenium.WebElement;
//import org.openqa.selenium.support.FindBy;
//import org.openqa.selenium.support.PageFactory;
//
//public class ChatHome {
//    private WebDriver driver;
//
//    //Login Page
//    private By usernameLogin = By.id("usernameInput");
//    private By passwordLogin = By.id("passcodeInput");
//    private By loginButton = By.id("submitLogin"); // needs to be clicked twice
//    private By signupFirstName = By.id("signup-firstname");
//    private By signupLastName = By.id("signup-lastname");
//    private By signupEmail = By.id("signup-email");
//    private By signupBirthDate = By.id("signup-bdate");
//    private By signupUsername = By.id("signup-username");
//    private By signupPassword = By.id("signup-password");
//    private By signupButton = By.id("signup-submit"); //may need to be clicked twice
//
//
//    //Profile Page
//    private By friendSearchBar = By.id("search-inputbar");
//    private By friendSearchButton = By.id("searchButton");
//    private By createANewPost = By.id("updateProfileEditProfileBtn");
//    private By userImageFileInput = By.id("userImageFileInput");
//    private By updateProfileEditButton = By.id("updateProfileEditProfileBtn");
//    private By chatButton = By.className("linkChat");
//    private By groupButton = By.className("linkGroups");
//
//    //Chat Page
//    private By searchBox = By.id("search-container");
//
//
//    //Groups Page
//    private By groupName = By.id("groupName");
//    private By groupDescription = By.id("groupAbout");
//    private By addGroupButton = By.id("submitCreateGroup");
//    private By groupsButton = By.className("x-icon");
//
//    //Individual Groups Page
//    private By submitJoinGroup = By.id("submitJoinGroup");
//    private By whatsOnYourMind = By.id("postInput");
//    private By getWhatsOnYourMindButton = By.id("sendGroupPostButton");
//    private By leaveGroupButton = By.id("tbd");
//
//    public ChatHome(WebDriver driver){
//        this.driver = driver;
//        // the page factory abstracts away the logic for interacting with web elements
//        PageFactory.initElements(driver,this);
//    }
//
//    @FindBy(id = "js-link-box-en")
//    public WebElement english;
//
//
//    // you can also avoid using the page factory and manually search for the elements yourself
////    public void sendKeysToSearchbar(String input){
////        driver.findElement(searchBar).sendKeys(input);
////    }
////
////    public void clickSearchButton(){
////        driver.findElement(searchButton).click();
////    }
//
//}
