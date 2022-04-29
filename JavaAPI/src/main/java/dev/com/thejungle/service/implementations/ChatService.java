package dev.com.thejungle.service.implementations;

import dev.com.thejungle.customexception.InvalidInputException;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.service.interfaces.ChatServiceInt;

import java.util.ArrayList;

public class ChatService implements ChatServiceInt {

    private final ChatDAO chatDAO;

    public ChatService(ChatDAO chatDAO) {
        this.chatDAO = chatDAO;
    }

    /**
     * calls createMessage in ChatDao
     * @param chatMessage Object that contains information of the chat sent by the user
     * @return creating Message for the user using three parameters and looks through if they're less than zero or not.
     * If it is less than it will throw an exception
     */
    @Override
    public ChatMessage serviceCreateMessageObject(ChatMessage chatMessage){
        if(chatMessage.getUserId() <= 0){
            throw new InvalidInputException("Invalid User ID");
        } else if (chatMessage.getGroupId() < 0) {
            throw new InvalidInputException("Invalid Group ID");
        } else if (chatMessage.getChatContent().isEmpty()) {
            throw new InvalidInputException("Invalid Chat Content");
        } else if (chatMessage.getChatContent().length() > 300){
            throw new InvalidInputException("Long Content");
        } else {
            return chatDAO.createMessage(chatMessage);
        }
    }

    /**
     * calls getMessageHistory in ChatDAO for Group Chatroom
     * @param groupId id of group
     * @return ArrayList of ChatMessage objects from 5 minutes ago in group chat room
     * Will return empty ArrayList if no messages
     */
    @Override
    public ArrayList<ChatMessage> serviceGetMessageHistory(int groupId) {
        if (groupId < 1) {
            throw new InvalidInputException();
        }
        return chatDAO.getMessageHistory(groupId);
    }

    /**
     * calls getMessageHistory in ChatDAO for Global Chatroom
     * @return ArrayList of ChatMessage from 5 minutes ago in global chat room
     * Will return empty ArrayList if no messages
     */
    @Override
    public ArrayList<ChatMessage> serviceGetMessageHistory() {
        return chatDAO.getMessageHistory();
    }
}
