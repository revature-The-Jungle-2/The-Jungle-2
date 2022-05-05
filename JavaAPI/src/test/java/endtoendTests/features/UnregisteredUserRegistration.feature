Feature:
  Scenario: As an unregistered user i should be able to successfully create a profile
    Given i am on the registration page
    When i enter my profile info correctly
    When i click the registration submit button
    Then my profile is created and i am redirected to my profile page