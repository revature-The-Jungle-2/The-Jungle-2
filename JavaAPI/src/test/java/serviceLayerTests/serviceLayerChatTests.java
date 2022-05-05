package serviceLayerTests;


import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.service.implementations.ChatService;
import org.testng.annotations.Test;

import java.util.ArrayList;

public class serviceLayerChatTests {
    ChatService chatservice = new ChatService(new ChatDAO());


    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Group ID")
    public void serviceCreateMessageObjectInvalidGroupId() {
        ChatMessage chatMessage = new ChatMessage(1, -1, "message");
        chatservice.serviceCreateMessageObject(chatMessage);

    }

    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Long Content")
    public void serviceCreateMessageObjectInvalidChatContent() {
        ChatMessage chatMessage = new ChatMessage(1, 1, "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh");
        chatservice.serviceCreateMessageObject(chatMessage);  
    }

    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid User ID")
    public void serviceCreateMessageFailInvalidUserId(){
        ChatMessage chatMessage = new ChatMessage(0, 20, "Jungle");
        chatservice.serviceCreateMessageObject(chatMessage);
    }

    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Input Exception")
    public void serviceGetMessageHistoryNoGroupID(){
//        ArrayList<ChatMessage> testGetMessage = daoChatObject.getMessageHistory(-1);
        chatservice.serviceGetMessageHistory(0);
    }
}
