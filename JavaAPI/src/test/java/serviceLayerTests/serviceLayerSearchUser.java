package serviceLayerTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;

public class serviceLayerSearchUser {

    public static UserDAO userDAO = new UserDAO();
    public static UserService userService = new UserService(userDAO);
    User user = new User(4, "matt", "ballard", "mattballard@gmail.com", "matty", "password", "Not much to know", 464745600L, ".gif");

    @Test
    public void SearchUserNameFirstNameMatch(){
        ArrayList<User> result = userService.searchForUserService("matty");
        Assert.assertEquals(user.getFirstName(), "matt");
    }
    @Test
    public void SearchUserNameLastNameMatch(){
        ArrayList<User> result = userService.searchForUserService("matty");
        Assert.assertEquals(user.getLastName(), "ballard");

    }
    @Test
    public void searchUserNameEmailMatch(){
        ArrayList<User> result = userService.searchForUserService("matty");
        Assert.assertEquals(user.getEmail(), "mattballard@gmail.com");


    }
    @Test
    public void searchUserNameBirthdateMatch(){
        ArrayList<User> result = userService.searchForUserService("matty");
        Assert.assertEquals(user.getUserBirthdate(),464745600L);

    }
}
