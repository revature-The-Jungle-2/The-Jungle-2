package dataAccessTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

public class dataAccessCreateUserTests
{
    public UserDAO userDAOImp = new UserDAO();

    int min = 001;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min); //ex: "lilly" + b + "@gmail.com"
    int c = (int)(Math.random()*(max-min+1)+min);
    int d = (int)(Math.random()*(max-min+1)+min);
    int f = (int)(Math.random()*(max-min+1)+min);


    @Test
    public void CreateUserSuccess()
    {
        User newUser = new User(0, "Lillith", "Thompson", "lilly" + b + "@gmail.com", "LunaBear", "BearLuna", "There's not too much to know", 1574121600000L, ".gif");
        User result = userDAOImp.createNewUser(newUser);
        Assert.assertNotEquals(result.getUserId(), 0);
    }

}
