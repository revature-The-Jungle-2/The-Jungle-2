
Feature: As a user, user can join a group
  Scenario:I can join a group
     Given I am on the grouppage home page
     When click on the Groups on the side bar
     When I am on the individual group page
     When I click on the join group button
     Then I get a message joined the group successfully
