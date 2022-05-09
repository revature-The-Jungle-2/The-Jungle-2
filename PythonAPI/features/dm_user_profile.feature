Feature: As a User, I should be able to create and maintain a profile page that is visible to other users.

  Scenario Outline: As a user, I should be able to log in.
    Given I am on the login page
    When  I enter my <username>
    When  I enter my new <password>
    When  I click the login button
    Then I am on the profile page


    Examples:
      | username | password |
      | username | password |


  Scenario Outline: As a user, I should be able to update my profile picture.
    Given I am on the profile page
    When  I click the profile picture
    When  I choose my <new_profile_picture>
    Then  I am back on the profile page

    Examples:
      |  |  | new_profile_picture |
      |  |  | downloads/Husky.jpg |

  Scenario Outline:  As a user, I should not be able to incorrectly update my about me section.
    Given I am on the profile page
    When  I click the edit profile button
    When  I enter my <about_me> incorrectly
    When  I enter my <birthday>
    When  I click the save changes button
    Then  I click the close button

     Examples:
       |  |  | about_me      | birthday |
       |  |  | I am a person |          |


  Scenario Outline:  As a user, I should not be able to incorrectly update my birthday section.
    Given I am on the profile page
    When  I click the edit profile button
    When  I enter my <about_me>
    When  I enter my <birthday> incorrectly
    When  I click the save changes button
    Then  I click the close button

     Examples:
       |  |  | about_me                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | birthday |
       |  |  | thisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylong | 01011997 |

  Scenario Outline:  As a user, I should be able to update my about me and birthday sections.
    Given I am on the profile page
    When  I click the edit profile button
    When  I enter my <about_me>
    When  I enter my <birthday>
    When  I click the save changes button
    Then  I am on the profile page

    Examples:
      |  |  | about_me      | birthday |
      |  |  | I am a person | 01011997 |

  Scenario:  As a User, I should be able to go to another user's profile
    Given I am on the profile page
    When  I click on my follower
    Then  I am on their profile

