package dev.com.thejungle.customexception;

public class DuplicateUsername extends RuntimeException {

    public DuplicateUsername (String message) {
        super(message);
    }

}
