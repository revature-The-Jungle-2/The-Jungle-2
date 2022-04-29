package dev.com.thejungle.customexception;

public class NoValuePasscode extends RuntimeException{
    public NoValuePasscode(String message) {
        super(message);
    }
}
