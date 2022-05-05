package serviceLayerTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.annotations.Test;

public class serviceLayerGetGroupsTests {

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceImp = new UserService(userDAOImp);



    @Test
    public void groupIdDoesNotExist(){

    }
    @Test
    public void groupNameTooLong(){

    }
}
