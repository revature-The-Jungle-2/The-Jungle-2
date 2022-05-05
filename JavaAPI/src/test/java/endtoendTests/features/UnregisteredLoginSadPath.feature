Feature: I should not be able to log in if I haven't created an account
  Scenario: As an un registered user i should not ba able to log in to access the profile page.
    Given i am on the login page
    When i enter a username
    When i enter a password
    When i click the login submit button
    Then i should be informed of incorrect credentials and remain on the login page