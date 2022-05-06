package endtoendTests.runner;




import endtoendTests.poms.ChatHome;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.time.Duration;
/*
    this class is what will handle running your E2E tests in Java. Make sure it is called TestRunner, because
    Cucumber will be looking for a class with that name to handle the setup and teardown for the test
 */

@RunWith(Cucumber.class) // this sets Cucumber as the framework to run our tests
@CucumberOptions(
        /*
            features: this determines which feature file/s will be used
            glue: this tells Cucumber where the step implementations are. Direct it to a package
            plugin: this is an optional setting we use to generate a nice html report of the test results
         */
        features = {"src/test/java/endtoendTests/features"},
//        glue = "src/test/java/endtoendTests/steps",
        glue = {"steps"},
        plugin = {"pretty","html:src/html-e2e-report.html"}
)
public class TestRunner {

    /*
        make your fields public static: at minimum you need a driver, make sure to add any poms here as well.
        You will also want to add any WebDriverWaits
     */

    public static WebDriver driver;
    public static ChatHome chatHome;
    public static WebDriverWait wait;


    @BeforeClass
    public static void setup(){
        // use the three lines below to set your driver
        File file = new File("chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        driver = new ChromeDriver();

            chatHome = new ChatHome(driver);
;


            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(1));
            wait = new WebDriverWait(driver,Duration.ofSeconds(4));
    }


    @AfterClass
    public static void teardown(){
        driver.quit();
    }

}