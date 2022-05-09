Feature:
  Scenario: As a registered user i should be able to log in to access my profile page
    Given i am on the log in page
    When i enter a username
    When i enter a password
    When i click the login submit button
    Then i am logged in and redirected to my profile page