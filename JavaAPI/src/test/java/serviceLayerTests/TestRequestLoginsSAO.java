package serviceLayerTests;

import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.service.implementations.UserService;

import dev.com.thejungle.customexception.*;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.annotations.Test;


public class TestRequestLoginsSAO {

    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceSAOImp = new UserService(userDAOImp);

    int min = 1;
    int max = 10000;
    int r = (int) (Math.random() * (max - min + 1) + min);
    int s = (int) (Math.random() * (max - min + 1) + min);
    int t = (int) (Math.random() * (max - min + 1) + min);
    int a = (int) (Math.random() * (max - min + 1) + min);
    int b = (int) (Math.random() * (max - min + 1) + min);
    int c = (int) (Math.random() * (max - min + 1) + min);
    int d = (int) (Math.random() * (max - min + 1) + min);
    int h = (int) (Math.random() * (max - min + 1) + min);
    int i = (int) (Math.random() * (max - min + 1) + min);
    int j = (int) (Math.random() * (max - min + 1) + min);
    int k = (int) (Math.random() * (max - min + 1) + min);


//    Login Service Access Layer (- UsernameTooLong
//              - PasscodeTooLong
//            - UserNamePasscodeNoMatch

//            - UserNameNoMatchUserId * doesn't make sense no ID in parameters or return
//            - PasscodeNoMatchUserId * doesn't make sense no ID in parameters or return


    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "You are exceeding your character limit")
    public void loginServiceUsernameTooLongNegative() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + r + "@gmail.com", "Thisisalongpasscode1029038347561029384756102938475610293847561029384756", "123", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }

    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "You are exceeding your character limit")
    public void loginServicePasscodeTooLongNegative() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + s + "@gmail.com", "mcb1", "Thisisalongpasscode1029038347561029384756102938475610293847561029384756", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }

    @Test(expectedExceptions = UsernameOrPasscodeException.class, expectedExceptionsMessageRegExp = "User Not Found")
    public void loginServiceUsernamePasswordNoMatchNegative() {
        User newUser = new User(1, "Lillith", "Thompson", "lilly" + h + "@gmail.com", "this_is_random", "nooneherebythatname", "There's not too much to know", 1574121600000L, ".gif");
        userServiceSAOImp.loginService(newUser.getUsername(), newUser.getPasscode());
    }
}