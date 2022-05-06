Feature: I can log into my profile page

  Scenario Outline: Users should be able to log in
    Given I am on the login page
    When I enter my <username> in the username box
    When I enter my <password> into the password box
    When I click the log-in button
    Then I am redirected to the profile page with <title>


    Examples:
      | username | password | title |  |
      | LunaBear | BearLuna | Login |  |
