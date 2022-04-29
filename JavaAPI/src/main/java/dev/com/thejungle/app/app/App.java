package dev.com.thejungle.app.app;

import dev.com.thejungle.app.appcontroller.appcontroller.AppController;
import dev.com.thejungle.app.appcontroller.controllers.ChatController;
import dev.com.thejungle.app.appcontroller.controllers.UserController;
import dev.com.thejungle.dao.implementations.ChatDAO;
import dev.com.thejungle.dao.implementations.UserDAO;
import dev.com.thejungle.service.implementations.ChatService;
import dev.com.thejungle.service.implementations.UserService;
import io.javalin.Javalin;

public class App {

    public static void main(String[] args) {
        Javalin app = Javalin.create(config -> {
            config.enableCorsForAllOrigins();
            config.enableDevLogging();
        });

        // Chat Controller
        ChatDAO chatDAO = new ChatDAO();
        ChatService chatService = new ChatService(chatDAO);
        ChatController chatController = new ChatController(chatService);

        // User Controller
        UserDAO userDAO = new UserDAO();
        UserService userService = new UserService(userDAO);
        UserController userController = new UserController(userService);

        // App Controller
        AppController appController = new AppController(app, chatController, userController);

        appController.createChatRoutes();
        appController.createUserRoutes();

        app.start();
    }

}

