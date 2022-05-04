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
     - Success                      [10.1]
     - UserIdFirstNameMatch         [10.2]
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
    - UserIdGroupIdNoMatch          [13.3]  <- returning a group that you aren't apart of>

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

# Deadline
 - May 05, 2022 Unit Testing
 - Postman
 - End to End
 - May 11, 20222 Code Freeze
 - May 12, 20222 for presentation
 