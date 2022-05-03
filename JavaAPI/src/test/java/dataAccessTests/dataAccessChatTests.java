package dataAccessTests;

import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;

public class dataAccessChatTests {


    ChatDAO chatDAO = new ChatDAO();


    @Test()
    public void createMessageChatIdSuccess() {

    ChatMessage chatMessage = new ChatMessage(1, 1, "Welcome");
    ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
    Assert.assertTrue(testCreateMessage.getUserId()!= 0);

    }


    @Test()
    public void createMessageGroupIdSuccess(){

        ChatMessage chatMessage = new ChatMessage(1,1,"Welcome");
        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
        Assert.assertTrue(testCreateMessage.getGroupId()!= 0);


    }

    @Test()
    public void createChatContentSuccess(){

        ChatMessage chatMessage = new ChatMessage(1,1,"Welcome");
        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
        Assert.assertEquals(testCreateMessage.getChatContent(), "Welcome");


    }
    @Test()
    public void getMessageHistorySuccess() {
        ArrayList<ChatMessage> testGetMessage = chatDAO.getMessageHistory(1);
        Assert.assertFalse(testGetMessage.isEmpty());
    }


}





