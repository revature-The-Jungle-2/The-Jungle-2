package serviceLayerTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.annotations.Test;

public class serviceLayerGetUserTests {
    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);



    @Test
    public void invalidUserName(){

    }
    @Test
    public void userIdUserNameMatch(){

    }
    @Test
    public void userIdBirthdayMatch(){

    }
    @Test
    public void userIdEmailMatch(){

    }
}
