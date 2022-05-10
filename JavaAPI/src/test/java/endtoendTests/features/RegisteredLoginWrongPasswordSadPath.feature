Feature: I should not be able to log in if I input incorrect credentials
  Scenario: As a registered user i should not be able to log in with an incorrect password
    Given i am on the login page
    When i fail to enter a correct password i am told the password must be correct
    When i click the login submit button
    Then i should be informed of incorrect credentials and remain on the login page