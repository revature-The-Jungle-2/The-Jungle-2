package EntityTests;

import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.entity.User;
import org.testng.Assert;
import org.testng.annotations.Test;

public class EntityChatMessageTests {

    ChatMessage chatMessage = new ChatMessage(1, "12-25-2022",1, "matty", 1,"Merry christmas");
    @Test
    public void UserEquals(){
        chatMessage.equals(new Object());
        Assert.assertFalse(chatMessage.equals(new Integer(1)));
    }
    @Test
    public void UserEqualsSuccess(){
        chatMessage.equals(new Object());
        Assert.assertTrue(chatMessage.equals(chatMessage));
    }
    @Test
    public void UserEqualsNewUser(){
        ChatMessage newChat = new ChatMessage(1, "12-25-2022",1, "matty", 1,"Merry christmas");
        Boolean isUser = chatMessage.equals(newChat);
        Assert.assertTrue(isUser);
    }
}
