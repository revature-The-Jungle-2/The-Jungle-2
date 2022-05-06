Feature:
  Scenario: As an unregistered user i should not be able to submit incomplete profile information
    Given i am on the registration page
    When i fail to enter a properly formatted email i am told the email must be present or in correct format
    Then i remain on the registration page
