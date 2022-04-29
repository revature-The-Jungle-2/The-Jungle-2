package dev.com.thejungle.dao.interfaces;


import dev.com.thejungle.entity.User;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


public interface UserDAOInt {

    User createNewUser(User user);

    User requestLogin(String username, String password);

    User getUserById(int userId);

    ArrayList<User> searchForUser(String username);

    List<User> getAllUsers();

    HashMap<Integer,String> getGroupsNames(int userId);

    ArrayList<Integer> getGroups(int userId);


}
