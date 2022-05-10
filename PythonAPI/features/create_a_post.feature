Feature: The ability to create a post
  Scenario: As a User, I should be able to create a post with text and images.
    Given I am logged in
    When I click to open the post modal
    When I enter the post text info
    When I enter the image info
    When I press the submit button
    Then Post is created