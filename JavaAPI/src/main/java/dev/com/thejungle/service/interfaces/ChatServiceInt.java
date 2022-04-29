package dev.com.thejungle.service.interfaces;

import dev.com.thejungle.entity.ChatMessage;

import java.util.ArrayList;

public interface ChatServiceInt {


    ChatMessage serviceCreateMessageObject(ChatMessage chatMessage);

    ArrayList<ChatMessage> serviceGetMessageHistory(int groupId);

    ArrayList<ChatMessage> serviceGetMessageHistory();
}
