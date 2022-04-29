package dev.com.thejungle.service.interfaces;

import dev.com.thejungle.entity.User;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public interface UserServiceInt {

    User createNewUserService(User user);

    User getUserByIdService(int userId);

    ArrayList<User> searchForUserService(String username);

    User loginService(String username, String passcode);

    List<User> getAllUsersService();

    HashMap<Integer, String> getGroupsNames(int userId);

    ArrayList<Integer> getGroups(int userId);

}
