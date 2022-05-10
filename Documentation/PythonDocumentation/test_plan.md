## Technologies Used
#### Backend
- PostgreSQL - 42.3.1
- Cucumber - 7.1.0
- Selenium - 4.1.1
- Python - 3.7+
- behave - 1.2.6
- Flask - 2.0.2
- Psycopg - 3.0.8
- pytest - 6.2.5
- MagicMock
- Frontend
- HTML 5
- CSS 3
- Javascript
- Postman
- DBeaver
- 
## Roles
	We split our team up by features. With 4 groups of 2 each group will work their feature e2e.
- As a User, I should be able to create or join a group/team where there can be collaborative posts only for the group/team to view. -> Vathsala Vijayaraghavan, Younghwan Choi 
- As a User, I should have a post feed that displays other user's posts. -> Jeryl Skinner, William Blair
- As a User, I should be able to create a post with text and images. -> Kenn Felix, Julio Jaquet
- As a User, I should be able to create and maintain a profile page that is visible to other users. -> Dylan Mercer, Andraey Pompey

## Deadlines
All Tests Written - Friday, May 6th
All Tests Ready for Presentation - Tuesday, May 10th
Code Freeze - end of day Tuesday, May 10th
Presentation - Thursday, May 12th

### Update user profile (Dylan, Andraey)
- Get user profile:
-     Success.
      User ID must be numeric.
      User not found.
- Update user profile: 
-     Success.
      Birthdate is not null.
      “About me” section has too many characters.
      User not found.
- Get user image:
-     Success.
      User ID must be numeric.
      User image not found.
- Update user image: 
-     Success.
      User ID must be numeric.
      Image must be a string format.
      User not found.
- Update user image format: 
-     Success.
      User ID must be numeric.
      Image format must be a string.
      User not found.
- Get user followers
-     Success
      User Id not found
      User Id numeric
- Get users following user
-     Success
-     User Id not found
-     User Id numeric
- Follow user
-     Success
-     User follower Id not found
-     User being followed Id not found
-     User follower Id numeric
-     User being followed id numeric
- Unfollow user
-     Success
-     User follower Id not found
-     User being followed Id not found
-     User follower Id numeric
-     User being followed id numeric

### Create a Post(Ken, Julio) Part 1(Ken)
- Create a post dal layer
 Create_post_image
PTest Success
 NTest PostNotFound For no post
 Get_post_image
Ptest Success
Ntest PostImageNotFound
Create a post Service layer
Create_post_image
Mock Sucess
Mock Fail with line 6 error
NTest PostIdMustBeInteger
Ntest ImageMustBeAString
 Get_post_image
Mock Sucess
Mock Fail for line 9
Ntest PostIdMustBeInteger
Create a post Api layer
Create_post_image
Ptest success
Ntest PostIdMustBeAnInteger
Ntest PostNotFound
Ntest ImageMustBeAString
Get_post_image
Ptest Success
Ntest PostIdMustBeAnInteger
Ntest PostImageNotFound


Create a post data access layer
Create_post
Positive test 
Negative test

Create a post Service layer
Create_post
Mock Success
Mock Fail
Negative Test PostIdMustBeInteger
Negative test PostTextMustBeString



As a User, I should be able to create or join a group where there can be collaborative posts only for the group to view.
Vathsala Vijayaraghavan, Younghwan Choi
		1.  Create Group
Positive test create group DAL
Positive test create group SL
Negative test for invalid group id SL
Negative test for invalid user id SL
Negative test for invalid group name for Null value SL
Negative test for invalid group name for length less than 3 characters SL
Negative test for invalid group name for length greater than 40 characters SL
Negative test for invalid string length for group about  greater than 500 characters SL
Negative test for invalid image SL
Negative test for invalid group image string length greater than 40 characters SL
Negative test for invalid group name already taken
		2.  Join Group
Positive test Join Group
Negative type error Int (groupid, userid) SL
Negative no group id SL
		3.  Get Creator 
Positive test get creator DAL  
Negative no group id SL
Negative type error Int SL
  

As a User, I should have a post feed that displays other user's posts.
Jeryl Skinner, William Blair
get_all_posts
Delete_a_post
Get_all_posts_with_user_id

As a User, I should be able to create a post with text and images.
Kenn Felix, Julio Jaquet

## We are NOT testing …

## Stretch Goals
- 

