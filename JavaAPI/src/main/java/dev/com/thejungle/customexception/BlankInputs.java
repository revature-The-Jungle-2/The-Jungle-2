package dev.com.thejungle.customexception;

public class BlankInputs extends RuntimeException {

    public BlankInputs(String message) {
        super(message);
    }

}
