package dataAccessTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

public class dataAccessGetUserTests
{
    public UserDAO userDAOImp = new UserDAO();

    int min = 001;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min); //ex: "lilly" + b + "@gmail.com"
    int c = (int)(Math.random()*(max-min+1)+min);
    int d = (int)(Math.random()*(max-min+1)+min);
    int f = (int)(Math.random()*(max-min+1)+min);


    // Positive Test
    // Get user test displays/tests all individual requirements of (Get User Tests)
    @Test
    public void SearchUserByIDSuccess()
    {
        User testUser = userDAOImp.getUserById(3);
        User newUser = new User(3, "first", "last", "email@something.net", "newuser", 1903-01-02);
        Assert.assertEquals(testUser,newUser);
    }







            /////////////// Need to implement dao methods /////////////////
    // Positive Test
    // Note: DAO imp does not have search for first name. May need to implement it.
    @Test
    public void SearchUserByFirstNameSuccess()
    {
        User testUser = userDAOImp.getUserByFirstName("first");
        User newUser = new User(3, "first", "last", "email@something.net", "newuser", 1903-01-02);
        Assert.assertEquals(testUser,newUser);
    }

    // Positive Test
    @Test
    public void SearchUserByLastNameSuccess()
    {
        User testUser = userDAOImp.getUserByLastName("last");
        User newUser = new User(3, "first", "last", "email@something.net", "newuser", 1903-01-02);
        Assert.assertEquals(testUser,newUser);
    }

}
