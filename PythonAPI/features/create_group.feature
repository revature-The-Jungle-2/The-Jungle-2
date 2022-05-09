Feature: As a user, user can create a new group.

  Scenario Outline: I can create a group
    Given I am on the grouppage home page
    When I enter the <groupname> in the group name text box
    When I enter the <description> in the description text box
    When I click the Add Group button
    Then I get a message created the group successfully

    Examples:
      | groupname | description      |
      | noname    | not much to know |


