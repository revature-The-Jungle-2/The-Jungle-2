package dataAccessTests;

import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import org.eclipse.jetty.server.UserIdentity;
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
    public void CreateMessageWrongGroupId(){
        ChatMessage chatMessage = new ChatMessage(1,0,"Welcome");
        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
        Assert.assertEquals(testCreateMessage.getChatContent(), "Welcome");

    }

    @Test()
    public void getMessageHistoryGroupIdSuccess(){
        ArrayList<ChatMessage> testGetMessage = chatDAO.getMessageHistory(1);
        Assert.assertFalse(testGetMessage.isEmpty());
    }


    @Test
    public void getMessageHistoryWrongGroupId(){
        ArrayList<ChatMessage> testGetMessage = chatDAO.getMessageHistory(-1);
        Assert.assertTrue(testGetMessage.isEmpty());
    }

    @Test
    public void getMessageHistoryFailGroupId() {
        ArrayList<ChatMessage> testGetMessage = chatDAO.getMessageHistory();
        Assert.assertFalse(testGetMessage.isEmpty());
    }




}





