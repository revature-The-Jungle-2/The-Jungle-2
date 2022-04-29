package dev.com.thejungle.customexception;

public class UsernameOrPasscodeException extends RuntimeException {
    public UsernameOrPasscodeException(String message) {
        super(message);
    }
}
