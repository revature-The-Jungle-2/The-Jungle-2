package serviceLayerTests;

import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.service.implementations.ChatService;
import org.junit.Assert;
import org.testng.annotations.Test;

public class serviceLayerChatTests {

    @Test()
    public void createChatSuccess()


    @Test(expectedExceptions = InvalidInputException, expectedExceptionsMessageRegExp = "Invalid User ID")
    public void serviceCreateMessageObjectInvalidUserId(){
        ChatMessage chatMessage = new ChatMessage();
        ChatMessage result = ChatService.serviceCreateMessageObject(chatMessage);
        Assert.assertNotSame(result.getUserId(int));
    }

    @Test(expectedExceptions = InvalidInputException, expectedExceptionsMessageRegExp = "Invalid Group ID")
    public void serviceCreateMessageObjectInvalidGroupId(){
        ChatMessage chatMessage = new ChatMessage();
        ChatMessage result = ChatService.serviceCreateMessageObject(chatMessage);
        Assert.assertNotSame(result.getGroupId(int));


    }
    )
}
