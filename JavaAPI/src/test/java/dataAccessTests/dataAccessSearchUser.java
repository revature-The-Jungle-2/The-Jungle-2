package dataAccessTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;

public class dataAccessSearchUser {
    public static UserDAO userDAO = new UserDAO();

    @Test
    public void searchUserSuccess() {
        ArrayList<User> result = userDAO.searchForUser("matty");
        Assert.assertTrue(result.size()>0);
    }
    @Test
    public void searchUserFailure(){
        ArrayList<User> result = userDAO.searchForUser("dumby");
        Assert.assertTrue(result.isEmpty());
    }
}
