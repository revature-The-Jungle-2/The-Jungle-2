package dev.com.thejungle.customexception;

public class DuplicateEmail extends RuntimeException {

    public DuplicateEmail(String message) {
        super(message);
    }

}
