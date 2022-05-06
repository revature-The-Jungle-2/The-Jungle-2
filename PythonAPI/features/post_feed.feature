

Feature:  View Post Feed feature
    Scenario: As a user, I want to view others' posts with the View Post Feed feature
        Given  I am on the Visit Profile Page
        When   I click on the "Search for Friends" button
        Then   I should be re-directed to the View Post Feed webpage



Feature:  Post Feed Features

    Scenario: Users can log in and see posts in their feed
        Given I am on the Login Page
        When I enter my Username
        When I enter my Password
        When I click Login
        Then I can see posts in my feed


    Scenario: Users can view others posts with the View Post Feed feature.
        Given  I am on the Visit Profile Page
        When   I click on the "Search for Friends" button
        Then   I can view the Post Feed for my friends



    Scenario: Users can delete a post by post id
        Given I am on the Profile Page
        When I input post id
        When I click Delete Post
        Then My post id deleted


