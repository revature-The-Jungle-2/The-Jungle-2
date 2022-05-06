package     serviceLayerTests;

import dev.com.thejungle.customexception.NoValuePasscode;
import dev.com.thejungle.customexception.UsernameOrPasscodeException;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.annotations.Test;

public class serviceLayerLoginTests{

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

    int min = 1;

    int max = 10000;

    int y = (int)(Math.random() *(max-min+1)+min);

    @Test(expectedExceptions = NoValuePasscode.class, expectedExceptionsMessageRegExp = "You must enter username and password")
    public void loginServiceUsernameEmpty(){
        User newUser = new User(15, "Daniel", "Kuczynski", "DanD"+ y + "@yahoo.com", "", "password1", "I'm a Banana", 1574121600000L,".jpeg");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }

    @Test(expectedExceptions = NoValuePasscode.class, expectedExceptionsMessageRegExp = "You must enter username and password")
    public void loginServicePasscodeEmpty(){
        User newUser = new User(15, "Daniel", "Kuczynski", "DanD"+y+"@yahoo.com", "DanDman", "", "I'm a Banana", 1574121600000L,".jpeg");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }
    @Test(expectedExceptions = UsernameOrPasscodeException.class, expectedExceptionsMessageRegExp = "User Not Found")
    public void loginServiceBadUserName(){
        User newUser = new User(4, "Matt", "Ballard", "something"+y+"@somwhere.com", "Matt", "password1", "I'm a Banana", 1574121600000L,".jpeg");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }
    @Test(expectedExceptions = UsernameOrPasscodeException.class, expectedExceptionsMessageRegExp = "User Not Found")
    public void loginServiceBadPasscode(){
        User newUser = new User(4, "Matt", "Ballard", "something"+y+"@somwhere.com", "Matty", "password2", "I'm a Banana", 1574121600000L,".jpeg");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }

}
