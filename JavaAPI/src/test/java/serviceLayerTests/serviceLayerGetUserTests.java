package serviceLayerTests;
import dev.com.thejungle.customexception.InvalidInputException;
import org.testng.annotations.Test;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;


public class serviceLayerGetUserTests
{
    public UserDAO userDAOImp = new UserDAO();
    public UserService userServiceSAOImp = new UserService(userDAOImp);
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
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Input: UserId Must Be A Non 0 Positive")
    public void SearchUserByNegativeID()
    {
        userServiceSAOImp.getUserByIdService(-1);
    }
    // Negative Test for get all users by group id


}
