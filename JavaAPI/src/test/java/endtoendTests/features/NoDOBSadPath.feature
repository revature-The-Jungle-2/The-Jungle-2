Feature:As an unregistered user I should not be able to submit incomplete profile information
  Scenario: As an unregistered user i should not be able to login with no DOB
    Given i am on the registration page
    When i fail to enter a DOB i am told the DOB must be present
    Then i remain on the registration page