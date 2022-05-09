Feature:
  Scenario: As a user i should be able to access and use the chat from my profile page
    Given i am logged in an on my profile page
    When i click on the chat link
    When i am on the chat page i enter a message in the message input
    When i click on the send message button
    Then my message is seen in the chat window