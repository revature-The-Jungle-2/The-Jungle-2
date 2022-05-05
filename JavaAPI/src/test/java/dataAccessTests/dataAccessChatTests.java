//package dataAccessTests;
//
//import dev.com.thejungle.dao.implementations.ChatDAO;
//import dev.com.thejungle.entity.ChatMessage;
//import org.eclipse.jetty.server.UserIdentity;
//import org.testng.Assert;
//import org.testng.annotations.Test;
//
//public class dataAccessChatTests {
//
//
//    ChatDAO chatDAO = new ChatDAO();
//
//
//    @Test()
//    public void createMessageChatIdSuccess() {
//
//    ChatMessage chatMessage = new ChatMessage(1, 1, "Welcome");
//    ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//    Assert.assertTrue(testCreateMessage.getUserId()!= 0);
//
//    }
//
//
//    @Test()
//    public void createMessageGroupIdSuccess(){
//
//        ChatMessage chatMessage = new ChatMessage(1,1,"Welcome");
//        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//        Assert.assertTrue(testCreateMessage.getGroupId()!= 0);
//
//
//    }
//
//    @Test()
//    public void createChatContentSuccess(){
//
//        ChatMessage chatMessage = new ChatMessage(1,1,"Welcome");
//        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//        Assert.assertEquals(testCreateMessage.getChatContent(), "Welcome");
//
//    }
//
//    //Duplicate ID
//
//    @Test()
//    public void createChatMessageDuplicateChatId(){
//        ChatMessage chatMessage = new ChatMessage(0,0,"Message");
//        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//        Assert.assertNull(testCreateMessage);
//
//    }
//
//    @Test()
//    public void createChatMessageDuplicateGroupID(){
//        ChatMessage chatMessage = new ChatMessage(0,0,"Message");
//        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//        Assert.assertNull(testCreateMessage);
//    }
//
//    @Test()
//    public void createChatMessageDuplicateChatContent(){
//        ChatMessage chatMessage = new ChatMessage(0,0,"Message");
//        ChatMessage testCreateMessage = chatDAO.createMessage(chatMessage);
//        Assert.assertNull(testCreateMessage);
//
//
//
//    }
//
//
//    @Test()
//    public void getMessageHistoryChatIdSuccess(){
//        ArrayList<ChatMessage> testGetMessage = chatDAO.getMessageHistory(0);
//        Assert.assertFalse(testGetMessage.isEmpty());
//    }
//
//}
//
//
//
//
//
