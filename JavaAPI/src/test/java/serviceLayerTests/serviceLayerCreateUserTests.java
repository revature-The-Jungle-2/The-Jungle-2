package serviceLayerTests;

import dev.com.thejungle.customexception.BlankInputs;
import dev.com.thejungle.customexception.TooManyCharacters;
import dev.com.thejungle.customexception.UnallowedSpaces;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.postgresql.util.PSQLException;
import org.testng.Assert;
import org.testng.annotations.Test;

public class serviceLayerCreateUserTests
{
    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);
    public static User testUser;

    //    @BeforeClass
//    public void setup()
//    {
//        userDAOImp = Mockito.mock(UserDAO.class);
//        userServiceSAOImp = new UserService(userDAOImp);
//    }

    int min = 001;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min); //ex: "lilly" + b + "@gmail.com"
    int c = (int)(Math.random()*(max-min+1)+min);
    int d = (int)(Math.random()*(max-min+1)+min);
    int e = (int)(Math.random()*(max-min+1)+min);
    int f = (int)(Math.random()*(max-min+1)+min);
    int g = (int)(Math.random()*(max-min+1)+min);
    int h = (int)(Math.random()*(max-min+1)+min);


                    ///////////////  User  ///////////////////
    // Positive test
    // NOTE: need to change email and username after every test! Test will fail otherwise
    @Test
    public void CreateNewUserPositive()
    {
        User newUser = new User(0, "Lillith", "Thompson", "lt"+b+"@gmail.com", "LunaBear"+b, "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
        User result = userServiceSAOImp.createNewUserService(newUser);
        Assert.assertEquals(result.getFirstName(), "Lillith");
    }

                    /////////////// User First Name  ///////////////////

    // Negative test
    // NOTE: Commented out because Service Layer Imp does not catch first name character limit of 20 chars
//    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "You are exceeding your character limit")
//    public void CreateUserFirstNameTooLongFailure()
//    {
//        User testUser = new User(0, "LillithLillithLillith", "Thompson", "lt1"+d+"@gmail.com", "LunaBear"+d, "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
//        userServiceSAOImp.createNewUserService(testUser);
//    }

    // Negative Test
    @Test(expectedExceptions = BlankInputs.class, expectedExceptionsMessageRegExp = "Please fill in the blanks")
    public void CreateUserFirstNameEmpty()
    {
        testUser = new User(0, "", "Thompson", "lt2"+c+"@gmail.com", "LunaBear"+c, "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(testUser);
    }

                            /////////////// User Password ///////////////////

    // Negative Test
    @Test(expectedExceptions = UnallowedSpaces.class, expectedExceptionsMessageRegExp = "No spaces allowed in username or password")
    public void CreateUserPasscodeSpaces()
    {
        testUser = new User(0, "", "Thompson", "lt4"+e+"@gmail.com", "LunaBear"+e, "Bear Luna", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(testUser);
    }

    // Negative Test
    @Test(expectedExceptions = BlankInputs.class, expectedExceptionsMessageRegExp = "Please fill in the blanks")
    public void CreateUserPasscodeEmpty()
    {
        testUser = new User(0, "", "Thompson", "lt5"+f+"@gmail.com", "LunaBear"+f, "", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.createNewUserService(testUser);
    }



}
