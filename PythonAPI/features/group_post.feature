Feature: I can log into my profile page, create a group post and delete a group post.
  Scenario: As a user, I should be able to log in.
    Given I am logged in
    When I am on the profile page and can see the post feed
    When I select groups
    When I select groups the second time
    Then I am on the page to make a group post

#  Scenario: Users can get all posts from group
#    Given  I am on the profile page
#    When I click on a group
#    Then I can see all posts in the group

#    Examples:
#      | title |  |
#      | Home  |  |


# Following features were not completed

#  Scenario Outline: Users can create a post
#    Given I am on the login page
#    When I enter my <username> in the username box
#    When I enter my <password> into the password box
#    When I click the log-in button
#    When I am redirected to the profile page with <title>
#    When I click on groups
#    When I click on groups again
#    When I enter a <comment>
#    When I click post
#    Then I have made a group post
#
#    Examples:
#      | username | password | title | comment    |
#      | LunaBear | BearLuna | Home  | Hi im Luna |
#
#
#  Scenario Outline: Users can not create a post that is too long
#    Given I am on the login page
#    When I enter my <username> in the username box
#    When I enter my <password> into the password box
#    When I click the log-in button
#    When I am redirected to the profile page with <title>
#    When I click on groups
#    When I click on groups again
#    When I enter a <comment>
#    When I click post
#    Then I have made a group post
#
#    Examples:
#      | username | password | title | comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
#      | LunaBear | BearLuna | Home  | thisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylongthisaboutmesectioniswaywaywaywaywaywaywaytoolongtopassthroughthecharactercheckingtestsoIwillmakeitextremelylong |