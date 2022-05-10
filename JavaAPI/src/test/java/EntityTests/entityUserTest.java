package EntityTests;

import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

public class entityUserTest {

    User user = new User(4, "Matt", "Ballard", "Something@something.com", "matty", "password", "Not Much to say", 1574121600000L, ".jpeg");

    @Test
    public void UserInfoUserIdTest() {
        user.setUserId(4);
        Assert.assertEquals(user.getUserId(), 4);
    }
    @Test
    public void UserInfoUserFirstNameTest() {
        user.setFirstName("Matt");
        Assert.assertEquals(user.getFirstName(), "Matt");
    }
    @Test
    public void UserInfoUserLastNameTest() {
        user.setLastName("Ballard");
        Assert.assertEquals(user.getLastName(), "Ballard");
    }
    @Test
    public void UserInfoUserUserNameTest() {
        user.setUsername("matty");
        Assert.assertEquals(user.getUsername(), "matty");
    }
    @Test
    public void UserInfoUserPasscodeTest() {
        user.setPasscode("password");
        Assert.assertEquals(user.getPasscode(), "password");
    }
    @Test
    public void UserInfoUserEmailTest() {
        user.setEmail("Something@something.com");
        Assert.assertEquals(user.getEmail(), "Something@something.com");
    }
    @Test
    public void UserInfoUserAboutMeTest() {
        user.setUserAbout("Not Much to say");
        Assert.assertEquals(user.getUserAbout(), "Not Much to say");
    }
    @Test
    public void UserInfoUserBirthdateTest() {
        user.setUserBirthdate(1574121600000L);
        Assert.assertEquals(user.getUserBirthdate(), 1574121600000L);
    }
    @Test
    public void UserEquals(){
        user.equals(new Object());
        Assert.assertFalse(user.equals(new Integer(5)));
    }
    @Test
    public void UserEqualsSuccess(){
        user.equals(new Object());
        Assert.assertTrue(user.equals(user));
    }
    @Test
    public void UserEqualsNewUser(){
        User newUser = new User(4, "Matt", "Ballard", "Something@something.com", "matty", "password", "Not Much to say", 1574121600000L, ".jpeg");
        Boolean isUser = user.equals(newUser);
        Assert.assertTrue(isUser);
    }
}