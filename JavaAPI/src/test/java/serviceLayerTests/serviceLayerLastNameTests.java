package serviceLayerTests;

import dev.com.thejungle.customexception.BlankInputs;
import dev.com.thejungle.customexception.TooManyCharacters;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.mockito.Mockito;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class serviceLayerLastNameTests {



    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
//    int c = (int)(Math.random()*(max-min+1)+min);
//    int d = (int)(Math.random()*(max-min+1)+min);
//    int f = (int)(Math.random()*(max-min+1)+min);



    //service layer is not catching for last name
    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "You are exceeding your character limit")
    public void userLastNameTooLong() {
        User newUser = new User(0, "Lillith", "Thompson!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "lilly" + b + "@gmail.com", "LunaBear", "BearLuna", "There's not too much to know", 1984 - 11 - 19, ".gif");
        userServiceSAOImp.createNewUserService(newUser);


        }
    @Test(expectedExceptions = BlankInputs.class, expectedExceptionsMessageRegExp = "Please fill in the blanks")
    public void userLastNameEmptyString() {
        User newUser = new User(0, "Lillith", "", "lilly" + b + "@gmail.com", "LunaBear", "BearLuna", "There's not too much to know", 1984 - 11 - 19, ".gif");
        userServiceSAOImp.createNewUserService(newUser);



    }

}