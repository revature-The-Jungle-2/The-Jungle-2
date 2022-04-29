package dev.com.thejungle.app.appcontroller.controllers;

import com.google.gson.Gson;
import dev.com.thejungle.customexception.*;
import dev.com.thejungle.entity.User;
import dev.com.thejungle.service.implementations.UserService;
import io.javalin.http.Handler;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class UserController {

    private UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    // Search User By UserName
    public Handler SearchUserByUsername = ctx -> {
        String username = ctx.pathParam("username");
        Gson gson = new Gson();
        try {
            ArrayList<User> users = this.userService.searchForUserService(username);
            if (users == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            }
            HashMap<String, ArrayList<User>> map = new HashMap<>();
            map.put("searchResult", users);
            String userJSON = gson.toJson(map);
            ctx.result(userJSON);
            ctx.status(200);
        } catch (InvalidInputException e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    // Get All Users
    public Handler getAllUsers = ctx -> {
        Gson gson = new Gson();
        try {
            List<User> users = this.userService.getAllUsersService();
            if (users == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            }
            String usersJSONs = gson.toJson(users);
            ctx.result(usersJSONs);
            ctx.status(200);
        } catch (UserNotFound e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    // Get User By Id
    public Handler getUserById = ctx -> {
        int userId = Integer.parseInt(ctx.pathParam("userId"));
        Gson gson = new Gson();
        try {
            User user = this.userService.getUserByIdService(userId);
            if (user == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            } else {
                String userJSON = gson.toJson(user);
                ctx.result(userJSON);
                ctx.status(200);
            }
        } catch (InvalidInputException e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        } catch (UserNotFound e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        } catch (UsernameOrPasscodeException e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    // Login User
    public Handler loginUser = ctx -> {
        Gson gson = new Gson();
        try {
            User credentials = gson.fromJson(ctx.body(), User.class);
            User user = this.userService.loginService(credentials.getUsername(), credentials.getPasscode());
            if (user == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            }
            String userLoginJSON = gson.toJson(user);
            ctx.result(userLoginJSON);
            ctx.status(200);
        } catch (Exception e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    // Get Groups
    public Handler getGroups = ctx -> {
        int userId = Integer.parseInt(ctx.pathParam("userId"));
        Gson gson = new Gson();
        try {
            Map<String, ArrayList<Integer>> map = new HashMap<>();
            ArrayList<Integer> groupIds = this.userService.getGroups(userId);
            if (groupIds == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            }
            map.put("groupIds", groupIds);
            String resultsJson = gson.toJson(map);
            ctx.result(resultsJson);
            ctx.status(200);
        } catch (InvalidInputException e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    public Handler getGroupsNames = ctx -> {
        Gson gson = new Gson();
        int userId = Integer.parseInt(ctx.pathParam("userId"));
        try {
            Map<Integer, String> map = this.userService.getGroupsNames(userId);
            String resultsJson = gson.toJson(map);
            ctx.result(resultsJson);
            ctx.status(200);
        } catch (InvalidInputException e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };

    // Register User
    public Handler registerUser = ctx -> {
        Gson gson = new Gson();
        try {
            User newUser = gson.fromJson(ctx.body(), User.class);
            User createdUser = this.userService.createNewUserService(newUser);
            if (createdUser == null) {
                HashMap<String, String> message = new HashMap<>();
                message.put("errorMessage", "Error processing request");
                ctx.result(gson.toJson(message));
                ctx.status(400);
            }
            String createdUserJson = gson.toJson(createdUser);
            ctx.result(createdUserJson);
            ctx.status(201);
        } catch (UnallowedSpaces e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        } catch (DuplicateEmail e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        } catch (DuplicateUsername e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        } catch (BlankInputs e) {
            HashMap<String, String> message = new HashMap<>();
            message.put("errorMessage", e.getMessage());
            ctx.result(gson.toJson(message));
            ctx.status(400);
        }
    };
}
