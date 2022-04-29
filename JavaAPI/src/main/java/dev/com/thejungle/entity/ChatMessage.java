package dev.com.thejungle.entity;

import java.util.Objects;

public class ChatMessage {

    private int chatId;
    private String chatDate;
    private int userId;
    private String userName;
    private int groupId;
    private String chatContent;

    public ChatMessage() {

    }

    public ChatMessage(int userId, int groupId, String chatContent) {
        this.setUserId(userId);
        this.setGroupId(groupId);
        this.setChatContent(chatContent);
    }

    public ChatMessage(int chatId, String chatDate, int userId, String userName, int groupId, String chatContent) {
        this.setChatId(chatId);
        this.setChatDate(chatDate);
        this.setUserId(userId);
        this.setUserName(userName);
        this.setGroupId(groupId);
        this.setChatContent(chatContent);
    }

    public int getChatId() {
        return chatId;
    }

    public void setChatId(int chatId) {
        this.chatId = chatId;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public int getGroupId() {
        return groupId;
    }

    public void setGroupId(int groupId) {
        this.groupId = groupId;
    }

    public String getChatDate() {
        return chatDate;
    }

    public void setChatDate(String chatDate) {
        this.chatDate = chatDate;
    }

    public String getChatContent() {
        return chatContent;
    }

    public void setChatContent(String chatContent) {
        this.chatContent = chatContent;
    }

    @Override
    public String toString() {
        return "ChatMessage{" +
                "chatId=" + chatId +
                ", chatDate='" + chatDate + '\'' +
                ", userId=" + userId +
                ", userName='" + userName + '\'' +
                ", groupId=" + groupId +
                ", chatContent='" + chatContent + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ChatMessage that = (ChatMessage) o;
        return chatId == that.chatId && userId == that.userId && groupId == that.groupId && Objects.equals(chatDate, that.chatDate) && Objects.equals(userName, that.userName) && Objects.equals(chatContent, that.chatContent);
    }

    @Override
    public int hashCode() {
        return Objects.hash(chatId, chatDate, userId, userName, groupId, chatContent);
    }
}
