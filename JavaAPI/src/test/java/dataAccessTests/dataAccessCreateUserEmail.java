package dataAccessTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.junit.Test;

public class dataAccessCreateUserEmail {
    public static UserDAO userDAO = new UserDAO();

    @Test()
    public void CreateUserEmailDuplicate()
    {
        User newUser = new User(0, "Lillith4", "Thompsotn", "lilly@gmail.com", "LunarBear", "BearLunar", "There's not too much to know", 1574121600000L, ".gif");
        userDAO.createNewUser(newUser);
        }
    }

