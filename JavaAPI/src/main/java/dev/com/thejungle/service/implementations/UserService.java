package dev.com.thejungle.service.implementations;

import dev.com.thejungle.customexception.*;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.interfaces.UserServiceInt;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class UserService implements UserServiceInt {

    private final UserDAO userDAO;

    public UserService (UserDAO userDAO) {
        this.userDAO = userDAO;
    }

    @Override
    public User createNewUserService(User user) {
        if (user.getUsername().matches(".*\\s+.*")) {
            throw new UnallowedSpaces("No spaces allowed in username or password");
        } else if (user.getPasscode().matches(".*\\s+.*")) {
            throw new UnallowedSpaces("No spaces allowed in username or password");
        } else if (user.getUsername().isEmpty() || user.getFirstName().isEmpty() || user.getLastName().isEmpty() ||
                user.getPasscode().isEmpty() || user.getEmail().isEmpty() || user.getUserBirthdate() == 0) {
            throw new BlankInputs("Please fill in the blanks");
        } else {
            return this.userDAO.createNewUser(user);
        }
    }

    @Override
    public ArrayList<User> searchForUserService(String username) {
        if (username.isEmpty()) {
            throw new InvalidInputException("Invalid Input: Empty Username");
        } else if (username.length() > 50) {
            throw new InvalidInputException("Invalid Input: UserName Exceeds 50 Characters");
        }
        return this.userDAO.searchForUser(username);
    }

    @Override
    public User getUserByIdService(int userId) {
        if (userId <= 0) {
            throw new InvalidInputException("Invalid Input: UserId Must Be A Non 0 Positive");
        }
        return this.userDAO.getUserById(userId);
    }

    @Override
    public User loginService(String username, String passcode) {
        if ((username.length() > 50) || (passcode.length() > 50))
            throw new TooManyCharacters("You are exceeding your character limit");
        if ((username.length() == 0) || (passcode.length() == 0))
            throw new NoValuePasscode("You must enter username and password");
        return this.userDAO.requestLogin(username, passcode);
    }


    @Override
    public List<User> getAllUsersService() {
        return this.userDAO.getAllUsers();
    }

    @Override
    public HashMap<Integer, String> getGroupsNames(int userId) {
        if (userId > 0) {
            return this.userDAO.getGroupsNames(userId);
        } else {
            throw new InvalidInputException("User Id needs to be positive");
        }
    }

    @Override
    public ArrayList<Integer> getGroups(int userId) {
        try {
            if (userId > 0) {
                if (userId < 1000000) {
                    return this.userDAO.getGroups(userId);
                } else {
                    throw new InvalidInputException("User Id needs to be positive and in range");
                }
            } else {
                throw new InvalidInputException("User Id needs to be positive and in range");
            }
        } catch (UserNotFound e) {
            throw new UserNotFound("User not found");
        }
    }
}

