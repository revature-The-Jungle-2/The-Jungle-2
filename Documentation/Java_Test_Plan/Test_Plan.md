# Technology
 - IntelliJ
 - Javalin
 - Postman
 - Dbeaver
 - Java
 - SQL
 - Mockito
 - Selenium
 - TestNG
 - L4J
 - Gson
 - GitHub
 - AWS EC2
 - Cucucmber - JUnit
 - Corretto 17
 - 

# Scope

## User Testing

### Create User Tests
+ Data Access Layer
    - Success Test                  [1.1]

    - createUerEmail                
        - Unique                    [3.1]

    - createUerUsername
        - Unique                   [4.1]

+ Service Layer

    - CreateUserFirstName
        - TooLong(20 char limit)    [1.2]
        - EmptyString               [1.3]

    - CreateUserLastName
        - TooLong(20 char limit)    [2.1]
        - EmptyString               [2.2]

    - CreateUserEmail
        - TooLong(50 char limit)    [3.2]
        - EmptyString               [3.3]
        - SpecialCharacters?        [3.4]
        - missingDomain             [3.5]

    - CreateUserUserName
        - TooLong(50 char limit)    [4.2]
        - EmptyString               [4.3]
        - Spaces                    [4.4]
        - 0                         [4.5]

    - CreateUserPasscode
        - TooLong(50 char limit)    [5.1]
        - EmptyString               [5.2]
        - Spaces                    [5.3]
        - 0                         [5.4]

    CreateUserAbout
        - TooLong(500 char limit)   [6.1]

    -CreateUserBirthdate
        - DateMonthOver12           [7.1]
        - DateDayOver31             [7.2]
        - DateYearOverCurrentYear   [7.3]
    
    - createUserimageFormat         [8.0]

### Request Login Tests
+ Data Access Layer
    - Success                       [9.1]

+ Service Access Layer
    - BlankInputs                   [9.2]
    - InvalidUsername               [9.3]
    - InvalidPasscode               [9.4]
    - EmptyStringUsername           [9.5]
    - EmptyStringPasscode           [9.6]
    - UsernameTooLong               [9.7]
    - PasscodeTooLong               [9.8]
    - UserNamePasscodeNoMatch       [9.9]
    - UserNameNoMatchUserId         [9.10]
    - PasscodeNoMatchUserId         [9.11]

### Get User Tests

+ Data Access Layer
    - Success                       [10.1]
    - UserIdFirstNameMatch          [10.2]
    - UserIdLastNameMatch           [10.3]
    - InvalidUsername               [10.4]
    - UserIDUsernameMatch           [10.5]
    - UserIdBirthdateMatch          [10.6]
    - UserIdEmailMatch              [10.7]

+ Service Access Layer
    - NegativeUserId                [10.8]


### Search For User

+ Data Access Layer
    - Success                       [11.1]
    
+ Service Access Layer
    - UserNameFirstNameMatch        [11.2]
    - UserNameLastNameMatch         [11.3]
    - UserNameEmailMatch            [11.4]
    - UserNameBirthdateMatch        [11.5]

### Get All Users

+ Data Access Layer
    - Success                       [12.1]

+ Service Access Layer 
    - EmailReturnsUsers             [12.2]
    - NegativeNumbers               [12.3]
    - BirthdateFormat               [12.4]
    - UsernameReturnsUsers          [12.5]
    - EmptyStringSearch             [12.6]

### Get Groups Names
+ Data Access Layer
    - Success                      [13.1]

+ Service Access Layer 
    - GroupDoesNotExist            [13.2]
    - UserIdGroupIdNoMatch         [13.3]  <- returning a group that you aren't apart of>

### Get Groups
+ Data Access Layer
    - Success                      [14.1]

+ Service Access Layer 
    - GroupIdDoesNotExist           [14.2]
    - GroupNameTooLong(40 chars)    [14.3]

## Chat Testing
### Create Message
+ Data Access Layer
    - Success                      [15.1]

+ Service Access Layer     
    - InvalidUserId                 [15.2]
    - InvalidGroupId                [15.3]
    - MessageTooLong(300 char)      [15.4]
    - InvalidChatContent            [15.5]
    - InvalidTimeStamp              [15.6]

### Get Message History
+ Data Access Layer
    - Success                      [16.1]
    - NegativeGroupId              [16.2]

+ Service Access Layer
    - ChatIdInvalid                    [16.3]

 ### End 2 End tests acceptance criteria/id information for POM
ogin page:
	username field: usernameInput
	password field: passcodeInput
	submit button: submitLogin
	
	registration link: /html/body/div/div/div[1]/div/div[4]/span/span/a

	error message p element invalid credential: errorMessageGoesHere
	error message p element no username: signup-invalid-message

profile-page:
	chat link: /html/body/div/div/div[5]/div[1]/a/span
	username search input box: searchInputBox
	username search button: searchButton
	drop down for username search results: searchList

chat page:
	chat window: chat-box
	chat message input field: message
	chat send button: send
	group chat link: //*[@id="1"]
	message inside of chat: //*[@id="chat"]/div/div

registration page:
	first name input field: signup-firstname
	last name input field: signup-lastname
	email input: signup-email
	bday input: signup-bdate
	username input: signup-username
	password input: signup-password
	error message p element: signup-invalid-message
	submit button: signup-submit
	<no error message for bad submission to api>


acceptance criteria for java functionality:
Feature:
Scenario: As an un registered user i should not ba able to log in to access the profile page.
Given i am on the login page
When i enter a username
When i enter a password
When i click the login submit button
Then i should be informed of incorrect credentials and remain on the login page

Scenario: As an unregistered user i should be able to register a profile for access to the profile page.
Given i am on the login page
When i click on the sign up link
Then i am redirected to the registration page


this scenario will need to e broken down for the actual testing into unique tests for the input or lack thereof

Scenario: As an unregistered user i should not be able to submit incomplete profile information
Given i am on the registration page
When i fail to enter a firstname i am told the firstname but be present
When i fail to enter a lastname i am told the lastname but be present
When i fail to enter a properly formtted email or leave the email blank i am told the email must be present or in correct format
When i fail to enter a DOB i am told the DOB must be present
When i fail to enter a properly formatted username or leave the username black i am told the username is missing or must be properly formatted
When i fail to enter a properly formatted password or leave the password black i am told the password is missing or must be properly formatted
Then i remain on the registration page

Scenario: As an unregistered user i should be able to successfully create a profile
Given i am on the registration page
When i enter my profile info correctly
When i click the registration submit button
Then my profile is created and i am redirected to my profile page

Scenario: As a registered user i should be able to log in to access my profile page
Given i am on the log in page
When i enter a username
When i enter a password
When i click the login submit button
Then i am logged in and redirected to my profile page

Scenario: As a user i should be able to access and use the chat from my profile page
Given i am logged in an on my profile page
When i click on the chat link
When i am on the chat page i enter a message in the message input
When i click on the send message button
Then my message is seen in the chat window

Scenario: As a user i should be able to access and use the group chat feature as well
Given i am logged in an on my profile page
When i click on the chat link
When i am on the chat page i click on a group chat link
When i click on the alert message informing me i am being switched to the group chat
Then i have access to a group chat


# Deadline
 - May 05, 2022 Unit Testing
 - May 05, 2022 Postman
 - May 09, 2022 End to End
 - May 11, 20222 Code Freeze
 - May 12, 20222 for presentation
 