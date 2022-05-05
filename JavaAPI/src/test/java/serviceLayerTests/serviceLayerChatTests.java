package serviceLayerTests;


import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.service.implementations.ChatService;
import org.testng.annotations.Test;

public class serviceLayerChatTests {
    ChatService chatservice = new ChatService(new ChatDAO());


    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Group ID")
    public void serviceCreateMessageObjectInvalidGroupId() {
        ChatMessage chatMessage = new ChatMessage(1, 1, "message");
        chatservice.serviceCreateMessageObject(chatMessage);

    }

    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Chat Content")
    public void serviceCreateMessageObjectInvalidChatContent() {
        ChatMessage chatMessage = new ChatMessage(1, 2, "message");
        chatservice.serviceCreateMessageObject(chatMessage);  
    }

    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid User ID")
    public void serviceCreateMessageFailInvalidUserId(){
        ChatMessage chatMessage = new ChatMessage(0, 20, "Jungle");
        chatService.serviceCreateMessageObject(chatMessage);
    }
}
  
