package dev.com.thejungle.app.appcontroller.controllers;

import com.google.gson.Gson;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.ChatService;
import io.javalin.websocket.WsConfig;
import io.javalin.websocket.WsContext;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;

public class ChatController {


    private Map<WsContext, Map> userUsernameMap = new ConcurrentHashMap<>();

    private ChatService chatService;

    public ChatController(ChatService chatService){
        this.chatService = chatService;
    }

    public void connectToWebSocket(WsConfig ws){
        ws.onConnect(ctx -> {
            ArrayList<ChatMessage> messages;
            int groupId=Integer.parseInt(ctx.pathParam("id"));
            String userName= ctx.pathParam("userName");
            Map<String,Object> userInfo = new HashMap<>();
            userInfo.put("groupId" , groupId);
            userInfo.put("userName", userName );
            userUsernameMap.put(ctx, userInfo);
            userListBroadcast(groupId);
            if(groupId == 0)
            {
                messages= chatService.serviceGetMessageHistory();
            }
            else{
                messages = chatService.serviceGetMessageHistory(groupId);
            }
            if(messages != null) {
                for (ChatMessage message : messages) {
                    broadcastMessage(message.getChatId(), message.getUserId(), message.getChatContent(), message.getUserName(), message.getChatDate(), message.getGroupId());
                }
            }
        });
        ws.onClose(ctx -> {
            userUsernameMap.remove(ctx);
            int groupId=Integer.parseInt(ctx.pathParam("id"));
            userListBroadcast(groupId);

        });
        ws.onMessage(ctx -> {
            System.out.println(ctx.message());
            Gson gson = new Gson();
            Map<Object,String> messageJson = gson.fromJson(ctx.message(), Map.class);
            System.out.println(messageJson);
            Double userIdDouble =  Double.parseDouble(messageJson.get("userId"));
            int userId = userIdDouble.intValue();
            int groupId = (Integer) userUsernameMap.get(ctx).get("groupId");

            String chatContent = messageJson.get("chatContent");
            String userName =messageJson.get("userName");
            ChatMessage chatMessage = new ChatMessage(userId,groupId,chatContent);
            ChatMessage returnedChat = chatService.serviceCreateMessageObject(chatMessage);
            broadcastMessage(returnedChat.getChatId(),returnedChat.getUserId(),returnedChat.getChatContent(),userName,returnedChat.getChatDate(),groupId);
        });
        ws.onBinaryMessage(ctx -> {
            int groupId = Integer.parseInt(ctx.pathParam("id"));
            String userName = ctx.pathParam("userName");
            ctx.data();
            sendImg(ctx.data(), groupId, userName);
        });

    };

    /**
     * sends to front-end a json of ChatMessage that the requesting user sent to other users in the same group chat
     * @param chatId id of chat
     * @param userId id of user
     * @param chatContent content of chat
     * @param userName username
     * @param date date the chat was sent
     * @param groupId id of group
     */
    public void broadcastMessage(int chatId, int userId, String chatContent,String userName,String date, int groupId) {

        userUsernameMap.keySet().stream().filter(ctx -> (ctx.session.isOpen() && (Integer) userUsernameMap.get(ctx).get("groupId") == groupId)).forEach(session -> {
            System.out.println(session);
            Gson gson = new Gson();
            Map<String, Object> broadcastString = new HashMap<>();
            broadcastString.put("chatId",chatId);
            broadcastString.put("userId",userId);
            broadcastString.put("chatContent", chatContent);
            broadcastString.put("userName", userName);
            broadcastString.put("date",date);
            session.send(gson.toJson(broadcastString));
        });
    }

    /**
     * sends to front-end a list of users that are in a specific group chat given the groupId.
     * @param groupId used to filter users by groups
     */
    public void userListBroadcast(int groupId){
        ArrayList<String> userList = new ArrayList();
        userUsernameMap.keySet().stream().filter(ctx -> (ctx.session.isOpen() && (Integer) userUsernameMap.get(ctx).get("groupId") == groupId)).forEach(session -> {
           for(Map<String,Object> a : userUsernameMap.values()){
               if((int)a.get("groupId") == groupId){
                   userList.add((String) a.get("userName"));
               }
           }
            Gson gson = new Gson();
            Map<String, Object> broadcastString = new HashMap<>();
            broadcastString.put("userList",userList);
            session.send(gson.toJson(broadcastString));

        });
    }

    /**
     * sends to front-end a byte[] of Img with its Base64 string
     * @param imgSent image
     * @param groupId id of group
     */
    public void sendImg(byte[] imgSent, int groupId, String userName){
        userUsernameMap.keySet().stream().filter(ctx -> (ctx.session.isOpen() && (Integer) userUsernameMap.get(ctx).get("groupId") == groupId)).forEach(session->{
            System.out.println(session);
            Map<String, Object> broadcastString = new HashMap<>();
            broadcastString.put("imgContent", imgSent);
            broadcastString.put("userName", userName);
            session.send(broadcastString);
        });
    }

}
