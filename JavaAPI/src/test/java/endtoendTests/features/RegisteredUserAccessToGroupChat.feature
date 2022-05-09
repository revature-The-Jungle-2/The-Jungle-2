Feature:
Scenario: As a user i should be able to access and use the group chat feature as well
  Given i am logged in an on my profile page
  When i click on the chat link
  When i am on the chat page i click on a group chat link
  When i click on the alert message informing me i am being switched to the group chat
  Then i have access to a group chat