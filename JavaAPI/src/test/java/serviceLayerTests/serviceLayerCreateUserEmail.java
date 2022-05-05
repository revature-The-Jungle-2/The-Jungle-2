package java.serviceLayerTests;

import dev.com.thejungle.dao.implementations.*;
import dev.com.thejungle.entity.*;
import dev.com.thejungle.service.implementations.*;
import org.junit.Test;

public class serviceLayerCreateUserEmail
{
    public UserDAO userDAO = new UserDAO();
    public UserService userService = new UserService(userDAO);
    public static User testUser;

    @Test
    public void CreateUserEmailTooLong(){
        User newUser = new User(0, "Adam", "West", "thisemailisactuallydefinitelywaytoolongtobearealemial@gmail.com", "Batman", "IamTheKnight", "I AM BATMAN", 1574121600000L, ".jpeg");
        userService.createNewUserService(newUser);
    }
    @Test
    public void CreateUserEmailEmptyString(){
        User newUser = new User(0, "Adam", "West", "", "TheBatman", "IAmTheKnight", "I AM BATMAN", 1574121600000L, ".jpeg");
        userService.createNewUserService(newUser);
    }
    @Test
    public void CreateUserEmailSpecialChar(){
        User newUser = new User(0, "Adam", "West", "!@#$%^&&*@aol.com", "TheBatman", "IAmTheKnight", "I AM BATMAN", 1574121600000L, ".jpeg");
        userService.createNewUserService(newUser);
    }
    @Test
    public void CreateUserEmailEmptyDomain() {
        User newUser = new User(0, "Adam", "West", "TheBatman@gmail", "TheBatman", "IAmTheKnight", "I AM BATMAN", 1574121600000L, ".jpeg");
        userService.createNewUserService(newUser);
    }
}
