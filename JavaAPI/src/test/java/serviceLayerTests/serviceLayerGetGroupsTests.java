package serviceLayerTests;

import dev.com.thejungle.customexception.BlankInputs;
import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.customexception.UserNotFound;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.HashMap;

public class serviceLayerGetGroupsTests {

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
    int f = (int)(Math.random()*(max-min+1)+min);


    // Negative Test
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "User Id needs to be positive and in range")
    public void getGroupOutOfRangeIDFailure()
    {
        userServiceSAOImp.getGroups(1000060);
    }

    // Negative Test
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "User Id needs to be positive and in range")
    public void getGroupNegativeIDFailure()
    {
        userServiceSAOImp.getGroups(-10);
    }

    // Negative Test
    @Test(expectedExceptions = UserNotFound.class, expectedExceptionsMessageRegExp = "User not found")
    public void getGroupNamesFailure()
    {
        userServiceSAOImp.getGroupsNames(100);
    }


}
