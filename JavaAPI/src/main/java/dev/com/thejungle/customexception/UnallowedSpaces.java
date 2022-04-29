package dev.com.thejungle.customexception;

public class UnallowedSpaces extends RuntimeException {

    public UnallowedSpaces(String message) {
        super(message);
    }

}
