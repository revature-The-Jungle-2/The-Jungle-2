package dev.com.thejungle.dao.implementations;

import dev.com.thejungle.dao.interfaces.ChatDAOInt;
import dev.com.thejungle.entity.ChatMessage;
import dev.com.thejungle.utility.ConnectionDB;

import java.sql.*;
import java.util.ArrayList;

public class ChatDAO implements ChatDAOInt {

    /**
     * connects to database to create a new ChatMessage
     * @param chatMessage Object that contains information of the chat sent by the user
     * @return ChatMessage that was created in the database
     */
    @Override
    public ChatMessage createMessage(ChatMessage chatMessage) {
        try (Connection connection = ConnectionDB.createConnection()) {
            if(chatMessage.getGroupId() == 0) {
                String sql = "insert into chat_log_table values(default, default, ?, null, ?) returning chat_id, chat_date";
                PreparedStatement preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setInt(1, chatMessage.getUserId());
                preparedStatement.setString(2, chatMessage.getChatContent());
                ResultSet resultSet = preparedStatement.executeQuery();
                resultSet.next();
                return new ChatMessage(
                        resultSet.getInt("chat_id"),
                        resultSet.getString("chat_date"),
                        chatMessage.getUserId(),
                        chatMessage.getUserName(),
                        chatMessage.getGroupId(),
                        chatMessage.getChatContent()
                );
            } else {
            String sql = "insert into chat_log_table values(default, default, ?, ?, ?) returning chat_id, chat_date";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, chatMessage.getUserId());
            preparedStatement.setInt(2, chatMessage.getGroupId());
            preparedStatement.setString(3, chatMessage.getChatContent());
            ResultSet resultSet = preparedStatement.executeQuery();
            resultSet.next();
            return new ChatMessage(
                    resultSet.getInt("chat_id"),
                    resultSet.getString("chat_date"),
                    chatMessage.getUserId(),
                    chatMessage.getUserName(),
                    chatMessage.getGroupId(),
                    chatMessage.getChatContent()
            );}
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * connects to database to retrieve messages from 5 minutes ago in group chat
     * @param groupId id of group
     * @return ArrayList of ChatMessage objects from 5 minutes ago in group chat room
     * Will return empty ArrayList if no messages
     */
    @Override
    public ArrayList<ChatMessage> getMessageHistory(int groupId) {
        try (Connection connection = ConnectionDB.createConnection()) {
                String sql = "select chat_id, chat_date, clt.user_id, ut.username, group_id, chat_content from chat_log_table clt " +
            "inner join user_table ut on ut.user_id = clt.user_id " +
            "where clt.chat_date >= now() - interval '5 minutes' and group_id = ? " +
                        "order by chat_id asc";
                PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, groupId);
                ResultSet resultSet = preparedStatement.executeQuery();
            ArrayList<ChatMessage> chatMessages = new ArrayList<>();
            while (resultSet.next()) {
                chatMessages.add(new ChatMessage(
                        resultSet.getInt("chat_id"),
                        resultSet.getString("chat_date"),
                        resultSet.getInt("user_id"),
                        resultSet.getString("username"),
                        resultSet.getInt("group_id"),
                        resultSet.getString("chat_content")
                ));
            }
            return chatMessages;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * connects to database to retrieve messages from 5 minutes ago in global chat
     * @return ArrayList of ChatMessage objects from 5 minutes ago in group chat room
     * Will return empty ArrayList if no messages
     */
    @Override
    public ArrayList<ChatMessage> getMessageHistory() {
        try (Connection connection = ConnectionDB.createConnection()) {
            String sql = "select chat_id, chat_date, clt.user_id, ut.username, group_id, chat_content from chat_log_table clt " +
                    "inner join user_table ut on ut.user_id = clt.user_id " +
                    "where clt.chat_date >= now() - interval '5 minutes' and group_id is null " +
                    "order by chat_id asc";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);
            ArrayList<ChatMessage> chatMessages = new ArrayList<>();
            while (resultSet.next()) {
                chatMessages.add(new ChatMessage(
                        resultSet.getInt("chat_id"),
                        resultSet.getString("chat_date"),
                        resultSet.getInt("user_id"),
                        resultSet.getString("username"),
                        resultSet.getInt("group_id"),
                        resultSet.getString("chat_content")
                ));
            }
            return chatMessages;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}