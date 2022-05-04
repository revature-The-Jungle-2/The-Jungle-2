package serviceLayerTests;

import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.Assert;
import org.testng.annotations.Test;

public class serviceLayerUserBirthdateTests {

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    int c = (int)(Math.random()*(max-min+1)+min);
    int d = (int)(Math.random()*(max-min+1)+min);
    int e = (int)(Math.random()*(max-min+1)+min);
    int f = (int)(Math.random()*(max-min+1)+min);
    int g = (int)(Math.random()*(max-min+1)+min);


// createNewUserService is not catching birthday format incorrectly type.
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Please enter correct birthday format")
    public void userBirthdayDateMonthOver12() {
            User userBirthdayMonth = new User(0, "Lillith", "Thompson", "lilly" + b + "@gmail.com", "LunaBear" + e, "BearLuna", "There's not too much to know", 1984 - 15 - 19, ".gif");
            userServiceSAOImp.createNewUserService(userBirthdayMonth);

    }
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Please enter correct birthday format")
    public void userBirthdayDateDayOver31(){
                User userBirthdayMonth = new User(0, "Lillith", "Thompson", "lilly" + c + "@gmail.com", "LunaBear"+ f, "BearLuna", "There's not too much to know", 1984 - 11 - 33, ".gif");
                userServiceSAOImp.createNewUserService(userBirthdayMonth);

        }


    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Please enter correct birthday format")
    public void userBirthdayDateYearOverCurrentYear(){
            User userBirthdayMonth = new User(0, "Lillith", "Thompson", "lilly" + d + "@gmail.com", "LunaBear" + g, "BearLuna", "There's not too much to know", 2023 - 11 - 19, ".gif");
            userServiceSAOImp.createNewUserService(userBirthdayMonth);

    }

    }


