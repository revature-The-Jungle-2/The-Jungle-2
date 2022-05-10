Feature:
  Scenario: As an unregistered user i should be able to register a profile for access to the profile page.
    Given i am on the registration page
    When i enter my profile info correctly
    When i click the registration submit button
    Then i am redirected to the profile page