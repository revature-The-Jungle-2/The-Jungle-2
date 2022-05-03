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

    - createUserFirstName
        - Success
    
    - createUserLastName
        - Success

    - createUerEmail
        - Success
        - Unique

    - createUerUsername
        - Success
         - Unique

    - createUserPasscode
        - Success

    - createUserUserAbout
        - Success

    - createUserUserBirthdate
        - Success

+ Service Layer

    - CreateUserFirstName
        - TooLong(20 char limit)
        - EmptyString

    - CreateUserLastName
        - TooLong(20 char limit)
        - EmptyString

    - CreateUserEmail

        - TooLong(50 char limit)
        - EmptyString
        - SpecialCharacters?
        - missingDomain

    - CreateUserUserName
        - TooLong(50 char limit)
        - EmptyString
        - Spaces
        - 0

    - CreateUserPasscode
        - TooLong(50 char limit)
        - EmptyString
        - Spaces
        - 0

    CreateUserAbout
        - TooLong(500 char limit)

    -CreateUserBirthdate
        - DateMonthOver12
        - DateDayOver31
        - DateYearOverCurrentYear
    
    - createUserimageFormat

### Request Login Tests
+ Data Access Layer
    - Success

+ Service Access Layer
    - BlankInputs
    - InvalidUsername
    - InvalidPasscode
    - EmptyStringUsername
    - EmptyStringPasscode
    - UsernameTooLong
    - PasscodeTooLong
    - UserNamePasscodeNoMatch
    - UserNameNoMatchUserId
    - PasscodeNoMatchUserId

### Get User Tests

+ Data Access Layer
     - Success

+ Service Access Layer
    - NegativeUserId
    - UserIdFirstNameMatch
    - UserIdLastNameMatch
    - InvalidUsername
    - UserIDUsernameMatch
    - UserIdBirthdateMatch
    - UserIdEmailMatch

### Search For User

+ Data Access Layer
    - Success
+ Service Access Layer
    - UserNameFirstNameMatch
    - UserNameLastNameMatch
    - UserNameEmailMatch
    - UserNameBirthdateMatch

### Get All Users

+ Data Access Layer
    - Success
+ Service Access Layer 
    - EmailReturnsUsers
    - NegativeNumbers
    - BirthdateFormat
    - UsernameReturnsUsers
    - EmptyStringSearch

### Get Groups Names
+ Data Access Layer
     - Success
+ Service Access Layer 
     - GroupDoesNotExist
    - UserIdGroupIdNoMatch <- returning a group that you aren't apart of>

### Get Groups
+ Data Access Layer
     - Success
+ Service Access Layer 
    - GroupIdDoesNotExist
    - GroupNameTooLong(40 chars)

## Chat Testing
### Create Message
+ Data Access Layer
     - Success
+ Service Access Layer     
    - InvalidUserId
    - InvalidGroupId
    - MessageTooLong(300 char)
    - InvalidChatContent(Empty Message?)
    - InvalidTimeStamp

### Get Message History
+ Data Access Layer
     - Success

+ Service Access Layer
 - ChatIdInvalid

# Deadline
 - Data Access Layer
 - Service Layer
 - Postman
 - End to End
 - May 11, 20222 Code Freeze
 - May 12, 20222 for presentation
 