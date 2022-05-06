Feature:
  Scenario: As an unregistered user i should not be able to submit incomplete profile information
    Given i am on the registration page
    When i fail to enter a properly formatted username i am told the username is missing or must be properly formatted
    Then i remain on the registration page