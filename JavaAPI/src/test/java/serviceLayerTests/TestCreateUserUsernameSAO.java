package serviceLayerTests;

import dev.com.thejungle.customexception.*;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.annotations.Test;

public class TestCreateUserUsernameSAO {

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    int c = (int)(Math.random()*(max-min+1)+min);
    int d = (int)(Math.random()*(max-min+1)+min);
    int f = (int)(Math.random()*(max-min+1)+min);
    int e = (int)(Math.random()*(max-min+1)+min);
    int g = (int)(Math.random()*(max-min+1)+min);
    int h = (int)(Math.random()*(max-min+1)+min);

    @Test(expectedExceptions = DuplicateUsername.class, expectedExceptionsMessageRegExp = "This username is already taken")
    public void createUserUsernameDuplicateUsernameServiceNegative() {
            User newUser = new User(1, "Lillith", "Thompson", "lilly" + b + "@gmail.com", "mcb1", "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
            userServiceSAOImp.createNewUserService(newUser);

    }
    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "value too long for type character varying(50)")
    public void createUserUsernameTooLongNegative() {
            User newUser = new User(1, "Lillith", "Thompson", "lilly" + c + "@gmail.com", "12345678900123456789012345678790123456789012345678901234567890", "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
            userServiceSAOImp.createNewUserService(newUser);
            //SAO and DAO do not catch this error
        }

    @Test(expectedExceptions = BlankInputs.class, expectedExceptionsMessageRegExp = "Please fill in the blanks")
    public void createUserUsernameBlankInputUsernameNegative() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + h + "@gmail.com", "", "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(newUser);

    }

    @Test(expectedExceptions = UnallowedSpaces.class, expectedExceptionsMessageRegExp = "No spaces allowed in username or password")
    public void createUserUsernameSpacesUsername() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + d + "@gmail.com", "lilly the lillith", "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(newUser);

    }

    @Test(expectedExceptions = UnallowedSpaces.class, expectedExceptionsMessageRegExp = "No spaces allowed in username or password")
    public void createUserUsernameSpacesNegative() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + e + "@gmail.com", "Lil", "Bear Luna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(newUser);

    }

    @Test(expectedExceptions = UnallowedSpaces.class, expectedExceptionsMessageRegExp = "0 can be a username")
    public void createUserUsernameZero() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + g + "@gmail.com", "0", "Bear Luna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(newUser);
        //0 passes, but it needs to be deleted and remade everytime
    }
}
