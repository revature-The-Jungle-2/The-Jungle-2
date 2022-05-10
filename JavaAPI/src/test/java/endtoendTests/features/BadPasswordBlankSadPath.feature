Feature:As an unregistered user I should not be able to submit incomplete profile information
  Scenario: As an unregistered user i should not be able to login with a blank password
    Given i am on the registration page
    When i leave the password blank i am told the password is missing or must be properly formatted
    Then i remain on the registration page