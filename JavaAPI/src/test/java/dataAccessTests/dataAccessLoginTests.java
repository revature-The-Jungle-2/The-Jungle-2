package dataAccessTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.junit.Test;
import org.testng.Assert;

public class dataAccessLoginTests
{   public static UserDAO userDAO = new UserDAO();

    @Test
    public void LoginSuccessTest()
    {
        userDAO.requestLogin("matty", "password");
        User result = userDAO.getUserById(4);
    }
}
