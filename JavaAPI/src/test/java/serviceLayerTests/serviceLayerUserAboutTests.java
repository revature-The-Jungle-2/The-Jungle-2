package serviceLayerTests;

import dev.com.thejungle.customexception.TooManyCharacters;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import org.testng.Assert;
import org.testng.annotations.Test;

public class serviceLayerUserAboutTests {
    public static UserDAO userDAOImp = new UserDAO();
    public static UserService userServiceImp = new UserService(userDAOImp);

    int min = 1;
    int max = 10000;
    int b = (int)(Math.random()*(max-min+1)+min);
    int c = (int)(Math.random()*(max-min+1)+min);




    @Test(expectedExceptions = TooManyCharacters.class, expectedExceptionsMessageRegExp = "")
    public void userAboutTooLong(){
            StringBuilder sb=new StringBuilder();
             while (sb.length() < 500){
            sb.append("There's not too much to know");}
            User newUserAbout = new User(0, "Lillith", "Thompson", "lilly" + b + "@gmail.com", "LunaBear" + c, "BearLuna", "There's not too much to know", 1984 - 11 - 19, ".gif");
            userServiceImp.createNewUserService(newUserAbout);



    }

}
