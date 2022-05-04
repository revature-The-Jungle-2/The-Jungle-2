package serviceLayerTests;

import dev.com.thejungle.customexception.BlankInputs;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.junit.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

public class TestGetAllUsersSAO {

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

//    Get ALL Users(Data Access Layer
//            SAL
//            - EmailReturnsUsers
//            - NegativeNumbers
//            - BirthdateFormat
//            - UsernameReturnsUsers
//            - EmptyStringSearch)


    @Test
    public void getAllUsersPositive() {
        List<User> lst = userServiceSAOImp.getAllUsersService();
        Assert.assertTrue(lst.size() >= 2);
    }

}
