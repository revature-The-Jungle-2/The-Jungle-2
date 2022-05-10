Feature: Delete post by post id
  Scenario: I can delete a post by post id
        Given I am on the my Profile Page
        When I input Post Id
        When I click Delete Post
        Then My post id is deleted



