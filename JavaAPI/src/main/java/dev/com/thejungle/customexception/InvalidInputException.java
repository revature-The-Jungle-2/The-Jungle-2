package dev.com.thejungle.customexception;

public class InvalidInputException extends RuntimeException {
    public InvalidInputException() {
        super("Invalid Input Exception");
    }

    public InvalidInputException(String message) {
        super(message);
    }
}
