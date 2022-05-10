Feature:  Post Feed Features
     Scenario Outline: As a user, I should be able to log in.
    Given I am on the group login page
    When  I enter my <username>
    When  I type in my new <password>
    When I click the welcome back
    When  I click the login button
    Then I am on the profile page


    Examples:
        | username | password |
        | LunaBear | BearLuna |