Feature:
Scenario: As a user i should be able to access and use the group chat feature as well
  Given i am logged in and on my profile page
  When i click on the chat button
  When i am on the chat page i click on a group chat link
  When i am on the group page and enter a group name
  When i am on the group page and enter a group description
  When i am on the group page i click on the add group button
  Then i have access to a that group