Feature:  Post Feed Features
    Scenario: Users can log in to their Profile Page
        Given I am on the Login Page
        When I enter my Username
        When I enter my Password
        When I click Login
        Then I am redirected to my Profile Page

    Scenario: Users can view posts with by User Id
        Given  I am on the my Profile Page
        When   I input User Id
        When I click Search For Friends
        Then   I can view the Post Feed for User Id

    Scenario: I can delete a post by post id
        Given I am on the my Profile Page
        When I input Post Id
        When I click Delete Post
        Then My post id is deleted