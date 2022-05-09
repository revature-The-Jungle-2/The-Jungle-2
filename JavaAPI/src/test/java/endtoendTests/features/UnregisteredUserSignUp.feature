Feature:
  Scenario: As an unregistered user i should be able to register a profile for access to the profile page.
    Given i am on the login page
    When i click on the sign up link
    Then i am redirected to the registration page