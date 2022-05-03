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
- createUserFirstName
    - Success
    - TooLong(20 char limit)
    - EmptyString
- createUserLastName
    - Success
    - TooLong(20 char limit)
    - EmptyString
- createUerEmail
    - Success
    - Unique
    - TooLong(50 char limit)
    - EmptyString
    - SpecialCharacters?
- createUerUsername
    - Success
    - Unique
    - TooLong(50 char limit)
    - EmptyString
    - Spaces
    - 0
- createUserPasscode
    - Success
    - TooLong(50 char limit)
    - EmptyString
    - Spaces
    - 0
- createUserUserAbout
    - Success
    - TooLong(500 char limit)
- createUserUserBirthdate
    - Success
    - DateMonthOver12
    - DateDayOver31
    - DateYearOverCurrentYear
- createUserimageFormat

### Request Login Tests
 - Success
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
 - Success
 - NegativeUserId
 - UserIdFirstNameMatch
 - UserIdLastNameMatch
 - InvalidUsername
 - UserIDUsernameMatch
 - UserIdBirthdateMatch
 - UserIdEmailMatch

### Search For User
 - Success
 - UserNameFirstNameMatch
 - UserNameLastNameMatch
 - UserNameEmailMatch
 - UserNameBirthdateMatch
 - 
### Get All Users
 - Success
 - EmailReturnsUsers
 - NegativeNumbers
 - BirthdateFormat
 - UsernameReturnsUsers
 - EmptyStringSearch

### Get Groups Names
 - Success
 - GroupDoesNotExist
 - UserIdGroupIdNoMatch <- returning a group that you aren't apart of>
 - 
### Get Groups
 - Success
 - GroupIdDoesNotExist
 - GroupNameTooLong(40 chars)

## Chat Testing
### Create Message
 - Success
 - InvalidUserId
 - InvalidGroupId
 - MessageTooLong(300 char)
 - InvalidChatContent(Empty Message?)
 - InvalidTimeStamp

### Get Message History
 - Success
 - ChatIdInvalid
 - 

# Deadline
 - Data Access Layer
 - Service Layer
 - Postman
 - End to End
 - May 11, 20222 Code Freeze
 - May 12, 20222 for presentation
 