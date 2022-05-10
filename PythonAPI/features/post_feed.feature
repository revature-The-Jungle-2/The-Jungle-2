Feature:  Post Feed Features
    Scenario: Users can log in to their Profile Page
        Given I am on the Login Page
        When I type in my Username
        When I enter my Password
        When I click Login
        When I am redirected to my Profile Page
        When I accept the alert
        Then I can view the Post Feed
po