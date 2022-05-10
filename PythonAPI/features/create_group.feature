Feature: As a user, user can create a new group and join to the group I want.
  Scenario Outline: I can create a group
    Given I am on the grouppage home page
    When I enter the groupname in the group name text box
    When I enter the <description> in the description text box
    When I click the Add Group button
    Then I get a message created the group successfully

    Examples:
      | description      |
      | not much to know |


  Scenario:I can join a group
    Given I am on the grouppage home page
     When click on the Groups on the side bar
     When I am on the individual group page
     When I click on the join group button
     Then I get a message joined the group successfully
