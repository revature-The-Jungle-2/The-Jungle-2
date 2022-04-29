package dev.com.thejungle.customexception;

public class TooManyCharacters extends RuntimeException{
    public TooManyCharacters(String message) {
        super(message);
    }
}
