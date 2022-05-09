package dataAccessTests;

import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.customexception.TooManyCharacters;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.HashMap;

public class dataAccessGetGroupsTests
{

    public static UserDAO userDAOImp = new UserDAO();

    // Positive Test
    //This gets/displays an array list of the group id a person is in by userID
    @Test
    public void getGroupSuccess()
    {
        ArrayList<Integer> result = userDAOImp.getGroups(1);
        Assert.assertTrue(result.size() >= 1);

    }

    // Negative Test
    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "No user exists with that ID")
    public void getGroupFailure()
    {
        userDAOImp.getGroups(100);
    }


    // Positive Test
    // This displays a hash map of the group id/name of the groups a person is in by userID
    @Test
    public void getGroupNamesSuccess()
    {
        HashMap<Integer, String> result = userDAOImp.getGroupsNames(1);
        Assert.assertTrue(result.size() >= 1);

    }







}
