package serviceLayerTests;
import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.service.implementations.ChatService;
import org.testng.annotations.Test;

public class serviceLayerChatTests {

    ChatService chatService = new ChatService(new ChatDAO());


    @Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid User ID")
    public void serviceCreateMessageFailInvalidUserId(){
        ChatMessage chatMessage = new ChatMessage(0, 20, "Jungle");
        chatService.serviceCreateMessageObject(chatMessage);
    }

    //@Test(expectedExceptions = InvalidInputException.class, expectedExceptionsMessageRegExp = "Invalid Chat Content")
    //public void serviceCreateMessageFailInvalidChatContent(){
      //  ChatMessage chatMessage = new ChatMessage(1,1," ");
       // chatService.serviceCreateMessageObject(chatMessage);









}