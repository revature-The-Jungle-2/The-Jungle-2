Feature:
  Scenario: As an unregistered user i should not be able to submit incomplete profile information
    Given i am on the registration page
    When i fail to enter a firstname i am told the firstname but be present
    When i fail to enter a lastname i am told the lastname but be present
    When i fail to enter a properly formatted email or leave the email blank i am told the email must be present or in correct format
    When i fail to enter a DOB i am told the DOB must be present
    When i fail to enter a properly formatted username or leave the username black i am told the username is missing or must be properly formatted
    When i fail to enter a properly formatted password or leave the password black i am told the password is missing or must be properly formatted
    Then i remain on the registration page