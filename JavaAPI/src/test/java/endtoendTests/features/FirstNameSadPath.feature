Feature:As an unregistered user I should not be able to submit incomplete profile information
  Scenario: As an unregistered user i should not be able to login with a blank first name
    Given i am on the registration page
    When i fail to enter a firstname i am told the firstname must be present
    Then i remain on the registration page